import re


class Node(object):
    """
    HTML태그 하나를 가지는 클래스
        내부에 다른 클래스를 가질수도 있음
        가장 큰 범위는 <html></html>
    """
    _pattern_tag_base = r'<{tags}.*?>\s*([.\w\W]*?)\s*</{tags}>'
    # private 으로 설정한다. 정규표현식의 패턴 압에 r을 입력해준다. 이스케이프 문자를 사용하여
    # 발생하는 충돌을 예방하기 위함이다.
    # < 안의 tag 와 이후 어떠한 문자열이 어떤 크기로 오는것과 무관하게 바로 따라오는 >표시까지이며
    # \s 공백을 고려한 괄호 안의 문자열을 그룹지정한다.
    # 단락을 나누는 공백을 제외한 모든 문자와 비문자를 그룹으로 지정하는데 그 크기는 상관없이
    # 해당 태그의 닫힘까지를 지정한다.
    _pattern_tag_content = r'<[^!]*?>([.\w\W]*)</.*?>'
    # 위와 동일한 구조이며 tag가 아닌 앞의 소스 시작부의 느낌표부를 제외한다.
    _pattern_tag_class = r'.*?class="([.\w\W].*?)"'
    def __init__(self, source):
        self.source = source
    # 초기화메서드를 정의하고 문자열 소스를 받는다.
    def __str__(self):
        return '{}\n{}'.format(
            super().__str__(),
            self.source
        )
    # 문자열메서드를 정의하는데
    def find_tag(self, tag):
    # find_tag 함수를 정의하고 매개변수로 tag값을 받는다.
        """
        주어진 tag 문자열, 또는 문자열의 리스트 반환
        :param tag: 검색을 원하는 태그. ex)'div'
        :param source: 태그를 검색할 전체 문자열
        :return: 검색 결과가 1개일 경우에는 tag문자열로 만든 Node객체, 2개 이상 일 경우에는 tag문자열로 만든 Node의 리스트
        """
        pattern = re.compile(self._pattern_tag_base.format(tags=tag))
    # source 에서 찾고자 하는 바를 패턴으로 지정하고 이를 미리 컴파일러하여 패턴확인을 빠르게한다.
    # pattern_tag_base 의 중괄호 속 tags 를 입력 받은 tag로 하여 컴파일한다.
        m_list = re.finditer(pattern, self.source)
    # finditer 문자열의 정규식 패턴에 대해 겹치지 않는 모든 일치 항목에 대해 반복자를 반환하여 m-list로 만든다.
        if m_list:
            return_list = [Node(m.group()) for m in m_list]
            return return_list if len(return_list) > 1 else return_list[0]
        return None
    # 조건문으로 앞서 만든 패턴에 속하는 전체를 (그룹에 따로 번호를 하지 않았으므로) 새로운 리스트로 만든다.
    # 이때 길이가 1 초과 즉, 두개부터 리스트로 나타내고 1개일때 해당 값을 직접 보인다.
    @property
    def content(self):
        """
        Node인스턴스의 내용을 리턴
        :return: Node(태그)내부의 내용 문자열을 리턴
        """
        pattern = re.compile(self._pattern_tag_content)
    # 앞서 find_tag와 다른 패턴을 갖는다. _ 를 하나 사용하여 보호되는 값임을 알 수 있다.
        m = re.search(pattern, self.source.strip())
    # 문자열 함수 strip을 통해 소스 문자열의 양쪽 공백을 지우고 패턴과 같은 값을 찾는다.
    # search 를 사용하여 첫번째 일치하는 패턴을 찾는다.
        if m:
            return m.group(1).strip()
    # 패턴에 사용된 괄호 안의 값들 (그룹의 숫자 1로 지정) 양옆의 공백을 지운 값을 반환한다.
        return None

    @property
    def class_(self):
        """
        해당 Node가 가진 class속성의 value를 리턴 (문자열)
        :return: 
        """
        pattern = re.compile(self._pattern_tag_class)
        m = re.findall(pattern, self.source.strip())
        if m:
            return m
        return None


with open('example.html') as f:
    html = Node(f.read())
    # 자동으로 파일을 닫기 위해 with 표현식 as 변수의 형태로 표현되었으며 해당 파일을 열고 전체를 읽어들인다.
node_div = html.find_tag('div')
    # html의 find_tag의 태그변수에 div를 넣고 node_div로 지정한다.
node_p_list = node_div.find_tag('p')
    # 마찬가지로 이번엔 p 태그에 대해 반복한다.
print(node_div.class_)
for node_p in node_p_list:
    print(node_p.content)
    # node_p를 content 실행시킨 값을 리턴받아 출력한다.

# pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
#
#
# def find_tag(tag, source):
#     """
#     주어진 tag 문자열, 또는 문자열의 리스트 반환
#     :param tag: 검색을 원하는 태그. ex)'div'
#     :param source: 태그를 검색할 전체 문자열
#     :return: 검색 결과가 1개일 경우에는 tag문자열, 2개 이상 일 경우에는 tag문자열의 리스트
#     """
#     pattern = re.compile(pattern_tag_base.format(tag=tag))
#     m_list = re.finditer(pattern, source)
#     if m_list:
#         return_list = [m.group() for m in m_list]
#         return return_list if len(return_list) > 1 else return_list[0]
#     return None
#
#
# # pattern_tag_content = r'^<.*?>([.\w\W]*?)</.*?>$'
# pattern_tag_content = r'<.*?>([.\w\W]*)</.*?>'
#
#
# def get_tag_content(tag_string):
#     """
#     tag 문자열이 주어졌을 때, 해당 tag의 내용을 리턴
#     :param tag_string: <tag>내용</tag>형태의 문자열
#     :return: 위 형태에서 '내용'부분
#     """
#     pattern = re.compile(pattern_tag_content)
#     m = re.search(pattern, tag_string.strip())
#     if m:
#         return m.group(1)
#     return None
#
#
# # html문자열 변수에서 'div'태그의 내용을 찾아 반환하는 함수 실행
# div = find_tag('div', html)
# p_list = find_tag('p', div)
# print(p_list)
# for p in p_list:
#     print(get_tag_content(p))
#
#
# # 원리
# pattern_div = re.compile(r'<div.*?>([.\w\W]*?)</div>')
# m = re.search(pattern_div, html)
# div = m.group(1)
#
# pattern_p = re.compile(r'<p.*?>([.\w\W]*?)</p>')
# m_list = re.finditer(pattern_p, div)