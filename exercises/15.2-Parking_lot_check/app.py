parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(lot):
    state = {"totalSlots": 0, "availableSlots": 0, "occupiedSlots": 0}
    for i in lot:
        for x in i:
            if x == 1:
                state["occupiedSlots"] += 1
                state["totalSlots"] += 1
            elif x == 2:
                state["availableSlots"] += 1
                state["totalSlots"] += 1
    return state

print(get_parking_lot(parking_state))
