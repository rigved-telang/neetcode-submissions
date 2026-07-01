class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = []
        fleet_cnt = 0
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        
        pos_speed.sort()

        for ps in pos_speed:
            stack.append(ps)

        while stack:
            curr = stack.pop()
            fleet_cnt += 1
            while stack and (target - stack[-1][0])/ stack[-1][1] <= (target - curr[0]) / curr[1]:
                stack.pop()
            
        
        return fleet_cnt
        
