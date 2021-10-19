def generate_child(curr_node,parent):
    childs = []
    if curr_node != None:
        for curr_jug in curr_node.value:
            if curr_jug.isEmpty():
                temp = []
                for temp_jug in curr_node.value:
                    copy_jug = copy.deepcopy(temp_jug)
                    if temp_jug == curr_jug:
                        copy_jug.fill_full_water()
                        temp.append(copy_jug)
                    else:
                        temp.append(copy_jug)
                childs.append(Node(copy.deepcopy(temp),[],curr_node))
            elif curr_jug.isFull():
                temp = []
                for temp_jug in curr_node.value:
                    copy_obj  = copy.deepcopy(temp_jug)
                    if temp_jug == curr_jug:
                        copy_obj.empty_jug()
                        temp.append(copy_obj)
                    else:
                        temp.append(copy.deepcopy(temp_jug))
                childs.append(Node(copy.deepcopy(temp),[],curr_node))
            if not curr_jug.isEmpty():
                for temp_jug in curr_node.value:
                    temp = []
                    if temp_jug != curr_jug:
                        if temp_jug.avail_space()  <= curr_jug.current_value():
                            for n in curr_node.value:
                                copy_obj = copy.deepcopy(n)
                                if n == curr_jug:
                                    copy_obj.pour_Water(temp_jug.avail_space())
                                    temp.append(copy_obj)
                                elif n == temp_jug:
                                    copy_obj.fill_Water(temp_jug.avail_space())
                                    temp.append(copy_obj)
                                else:
                                    temp.append(copy_obj)
                            childs.append(Node(copy.deepcopy(temp),[],curr_node))
                        elif temp_jug.avail_space()  > curr_jug.current_value():
                            for n in curr_node.value:
                                copy_obj = copy.deepcopy(n)
                                if n == curr_jug:
                                    copy_obj.pour_Water(curr_jug.current_value())
                                    temp.append(copy_obj)
                                elif n == temp_jug:
                                    copy_obj.fill_Water(curr_jug.current_value())
                                    temp.append(copy_obj)
                                else:
                                    temp.append(copy_obj)
                            childs.append(Node(copy.deepcopy(temp),[],curr_node))
        sort_childs(childs)    
        return childs
    else:
        return []                    
def sort_childs(childs,mode = 'asc'):
    pass


if __name__ == "mypackage.Gen_WJ":
    import copy
    from mypackage.Node import Node
    from mypackage.Jug import  Jug