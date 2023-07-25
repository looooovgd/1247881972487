nodeCost = [  # 간선들 간의 비용을 나타내는 리스트. 노드는 0~5번
    [0, 2, 5, 1, 99, 99],
    [2, 0, 3, 2, 99, 99],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, 99],
    [99, 99, 1, 1, 0, 2],
    [99, 99, 5, 99, 2, 0]
]
wentList = []
comparingList = [0, 99, 99, 99, 99, 99]  # 노드 0 번에서 시작하니까 0번 인덱스는 0으로 두었다.
current = 0  # 시작할 노드 번호.
distanceStack: int = 0
while 6 != len(wentList):
    wentList.append(current)  # 방문한 노드 추가
    tempList = []
    for i in range(6):  # 방문하지 않은 노드(가야 할 노드)들의 집합 만들기.
        if nodeCost[current][i] != 0 and nodeCost[current][i] != 99:
            if not wentList.count(i) > 0:
                tempList.append(i)

    for i in tempList:  # 가야할 노드 별로 cost를 비교해서 comparingList를 갱신.
        if nodeCost[current][i] + distanceStack < comparingList[i]:
            comparingList[i] = nodeCost[current][i] + distanceStack

    if len(tempList) == 0:
        break
    else: # 최소 거리인 값을 찾아 인덱스를 구하고, 거기로 이동하는 만큼 이동거리에 추가.
        tempCost = []
        for i in tempList: # 비용 비교용 배열인 tempCost만들기
            tempCost.append(nodeCost[current][i])
        tempIndex = 0
        distanceTemp = 99
        for i in range(len(tempList)):
            if tempCost[i] < distanceTemp :
                distanceTemp = tempCost[i] # 최소비용 찾을 때마다 넣기...
                tempIndex = tempList[i] # 인덱스도 넣기...
    distanceStack += distanceTemp
    current = tempIndex

print(wentList)
print(comparingList)