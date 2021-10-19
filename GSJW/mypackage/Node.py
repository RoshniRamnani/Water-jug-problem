class Node:
    def __init__(self):
        self.value = None
        self.children = []
        self.hueristic_value =None
        self.parent_node = None
    def __init__(self,value = None,children = [],parent = None):
        self.value = value
        self.children = children
        self.parent_node = parent
    def __repr__(self):
        return ",".join(list(map(str,self.value)))
    def hueristic_temp(self,GS):
        if self.value != None:
            amount_pouring = 0
            amount_filling = 0
            number_amount_pouring = 0
            number_amount_filling = 0
            sum_ = 0
            for i,(cur_Jug,GS_Jug) in enumerate(zip(self.value,GS)):
                if cur_Jug.value < GS_Jug.value:
                    amount_filling += abs(GS_Jug.value - cur_Jug.value) 
                    number_amount_filling +=1
                    sum_+=number_amount_filling
                elif cur_Jug.value > GS_Jug.value:
                    amount_pouring += abs(GS_Jug.value - cur_Jug.value)
                    number_amount_pouring -=1
                    sum_+= number_amount_pouring
            #print(f"p-{amount_pouring}-f{amount_filling}")
            if sum_ == 0:
                if amount_pouring == amount_filling:
                    sum_+=1
                else:
                    sum_-=1
                
            self.hueristic_value = sum_
            return sum_
    def hueristic_(self,GS):
        # first
        # if self.value != None:
        #     sum_with_weights=0
        #     sum_ = 1
        #     for  i,jug in enumerate(self.value):
        #         sum_with_weights += (jug.value * (i+2))
        #         sum_ += jug.value
        #     self.hueristic_value = sum_with_weights/sum_
        #     return sum_with_weights/sum_
        # second 
        # if self.value != None:
        #     sum_ = 0
        #     for i,(cur_Jug,GS_Jug) in enumerate(zip(self.value,GS)):
        #         if cur_Jug.value < GS_Jug.value:
        #             sum_+=(cur_Jug.value - GS_Jug.value) - i
        #         elif cur_Jug.value > GS_Jug.value:
        #             sum_+= (GS_Jug.value - cur_Jug.value)
        #         else :
        #             sum_+= (GS_Jug.value - cur_Jug.value)
        #     self.hueristic_value = sum_
        #     return sum_
        if self.value != None:
            amount_pouring = 0
            amount_filling = 0
            sum_ = 0
            for i,(cur_Jug,GS_Jug) in enumerate(zip(self.value,GS)):
                if cur_Jug.value < GS_Jug.value:
                    amount_filling += abs(GS_Jug.value - cur_Jug.value) 
                    sum_+=1
                elif cur_Jug.value > GS_Jug.value:
                    amount_pouring += abs(GS_Jug.value - cur_Jug.value)
                    sum_+= -1
            #print(f"p-{amount_pouring}-f{amount_filling}")
            if sum_ == 0:
                if amount_pouring == amount_filling:
                    sum_+=1
                else:
                    sum_-=1
            if self.check_val(GS):
                sum_+=1
            self.hueristic_value = sum_
            return sum_

    def check_val(self,Val):
        for i in range(len(self.value)):       
            #print(f"check_val_function_{self.value[i].value}---{Val[i].value}")
            if self.value[i].value != Val[i].value:
                return False
        return True
    def __str__(self) -> str:
        return ",".join(list(map(str,self.value)))
    def __lt__(self,other):
        #print(f"{self.hueristic_value}-------------{other.hueristic_value}--h")
        return self.hueristic_value < other.hueristic_value

