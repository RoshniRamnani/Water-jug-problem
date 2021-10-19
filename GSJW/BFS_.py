from mypackage.Node import Node
from mypackage.Jug import Jug
from mypackage.Gen_WJ import generate_child
import copy
class BFS:
    open_List = None
    close_List = None
    Init_Node = None
    goal_Node = None
    def __init__(self,IS,GS):
        self.open_List = []
        self.close_List = []
        self.Init_Node = IS
        self.Init_Node.parent_node = None
        self.goal_Node = GS
    def Find_path(self):
        if self.Init_Node != None and self.goal_Node != None:
            self.open_List.append(self.Init_Node)
            while self.open_List:
                curr_node = self.open_List.pop()
                if curr_node.check_val(self.goal_Node.value):
                    
                    traversal = []
                    traversal.append(curr_node)
                    temp_parent = curr_node.parent_node
                    while temp_parent != None:
                        traversal.append(temp_parent)
                        temp_parent = temp_parent.parent_node
                    
                    traversal.reverse()
                    print("\n".join(map(str,traversal)))
                    print("number of steps %d" % len(traversal))
                    print("goal node")
                    break
                else:
                    if (not self.check_for_open_list(curr_node)) and  (not self.check_for_close_list(curr_node)):
                        childs = generate_child(curr_node,curr_node.parent_node)
                        for child in childs:
                            child.parent_node = curr_node
                            child.hueristic_(self.goal_Node.value)
                            #print(f"{child} -------- {child.hueristic_value}")
                        childs = sorted(childs)
                        #print(childs)
                        #print(f"{curr_node}--------{childs}")
                        if len(childs) > 0:
                            self.open_List.extend(childs)
                            self.close_List.append(curr_node)
    def check_for_close_list(self,node):
        counter = 0
        for i in self.close_List:
        #print(f"call for check_val {' '.join(map(str,open_list))}")
            if not i.check_val(node.value):
                counter += 1
        #print(f"{counter}------{len(open_list)}")
        if counter == len(self.close_List):
            return False
        else:
            return True
    def check_for_open_list(self,node):
        counter = 0
        for i in self.open_List:
        #print(f"call for check_val {' '.join(map(str,open_list))}")
            if not i.check_val(node.value):
                counter += 1
        #print(f"{counter}------{len(open_list)}")
        if len(self.open_List) > 0:
            if counter == len(self.open_List):
                return False
            else:
                return True
        else:
            return False
if __name__ == "__main__":
    number_of_jug = int(input("Enter Number of Jug=>"))
    if number_of_jug >= 2:
        jug_size = input("Enter  Jug Size with comma as a seprator(Ex. 12,8,5,3,1 )=>").split(",")
        user_IS = input("Enter Initial state with comma as a seprator(Ex. 0,0,0,0,0 )=>").split(",")
        user_GS = input("Enter Goal state with comma as a seprator(Ex. 0,0,0,0,0 )=>").split(",")
        if len(user_IS) == len(user_GS) == number_of_jug == len(jug_size):
            IS_Jugs = []
            GS_Jugs = []
            for i in range(number_of_jug):
                IS_Jugs.append(Jug(int(jug_size[i]),int(user_IS[i])))
                GS_Jugs.append(Jug(int(jug_size[i]),int(user_GS[i])))
            bfs = BFS(Node(IS_Jugs),Node(GS_Jugs))
            bfs.Find_path()
        else:
            print("invalid Input")