'''
# 이진트리(binary tree)란?
- 모든 노드가 최대 2개의 자식만을 가질 수 있는 트리이다.
    -> 모든 노드의 차수가 2이하로 제한됨
- 자식 사이에도 순서가 존재, 왼쪽과 오른쪽 자식은 반드시 구별
- 계층적인 관계를 가진 모든 자료를 표현하기에는 부족
- 그러면 이진트리 언제 쓰는가?
    - 아주 빠른 자료의 탐색이 가능한 이진 탐색 트리(binary search tree)
    - 우선순위 큐를 효과적으로 구현하는 힙 트리(heap tree)
    - 수식을 트리의 형태로 표현하여 계산하는 수식 트리(expression tree)

# 이진트리의 종류
=> 트리 > 이진트리 > (완전 이진 트리 > 포화 이진 트리) / 경사 이진 트리
- 포화 이진 트리(full binary tree)
    - 각 레벨에 노드과 꽉 차있음
    - 노드의 개수를 쉽게 계산 가능
    - 각 노드에 순서대로 번호를 붙일 수 있다
    - 루트 노드의 번호는 항상 1, 왼쪽 자식은 2 오른쪽 자식은 3

- 완전 이진 트리(complete binary tree)
    - 높이가 k인 트리에서 레벨 1부터 k-1까지는 노드가 모두 채워져 있음
    - 마지막 레벨에서는 왼쪽부터 오른쪽으로 순서대로 노드가 채워져있어야함. 
    - 마지막 레벨에서는 노드가 꽉 차 있지 않아도 됨 but, 중간에 빈 곳은 없어야 한다.
    - ex)힙(heap)

- 균형 이진 트리(balanced binary tree)
    - 균형 이진 트리, 높이균형 이진 트리는 모든 노드에서 좌우 서브 트리의 높이 차이가 1 이하인 트리
        - 모든 노드에서 좌우 서브 트리의 높이 차이가 1이하여야 한다. 
        - 높이가 2 이상 차이나면 안됨 -> (2이상 차이나면 경사 이진 트리)

# 이진 트리의 표현 방법
1. 배열 구조 표현
- 노드에 번호를 붙이는 것을 그대로 배열의 인덱스로 사용한다.
    - 트리의 높이를 구해 배열(리스트)을 할당한다. 높이가 k일 때 (2의 k승 -1) 의 배열이 필요
    - 포화 이진트리의 번호를 인덱스로 사용하여 배열에 노드들을 저장
- 포화 이진 트리나 완전 이진 트리에 가장 적합하다.
- 일반 이진 트리도 표현 할 수 있지만 심한 경사 트리의 경우 배열 항목 사이에 빈칸이 많이 발생
    -> 메모리 낭비
- 이 표현법에서는 어떤 노드의 인덱스를 알면 부모 노드나 자식 노드의 인덱스를 쉽게 계산 가능하다.
    - 노드 i의 부모 노드 인덱스 = i//2
    - 노드 i의 왼쪽 자식 노드 인덱스 = 2i
    - 노드 i의 오른쪽 자식 노드 인덱스 = 2i+1
    
- 배열 표현법은 간단하지만 경사 트리에서 기억공간 낭비할 수 있다.
- 배열의 크기에 따라 표현 가능한 트리의 높이가 제한되는 단점이 있다.

2. 연결된 구조 표현 : 링크 표현법
- 이진 트리를 위한 노드는 두 개의 링크 필요, 각각 왼쪽 오른쪽 자식 노드를 가리킨다.
- 좌,우 링크 반드시 구별 !
- 링크 표현법에서 노드의 개수가 n이라면 None을 갖는 링크 수는 n-1개 이다.
'''

# 이진 트리를 위한 노드 클래스
class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left # 왼쪽 자식을 위한 링크
        self.right = right # 오른쪽 자식을 위한 링크