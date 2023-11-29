def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
   badges = []
   for name in names:
     message = f"Hello, my name is {name}."
     badges.append(message)
 
   return badges
       
def assign_rooms(names):
    badges = []
    for i, name in enumerate(names):
        room = i + 1 
        message = f"Hello, {name}! You'll be assigned to room {room}!"
        badges.append(message)

    return badges

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
        
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
