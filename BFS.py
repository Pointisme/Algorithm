def bfs(graph, start_node): #O(v+e)
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0) #앞에서부터 차례대로-->넓이가 우선순위이니까
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node): #O(v+e)
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()  #뒤에서부터 차례대로(숫자가 비교대상일때는 작은 값부터 먼저 찾기)
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))