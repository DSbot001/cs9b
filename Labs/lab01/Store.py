class Store:
    def __init__(self):
          self.items_dic = {}

    def addItem(self, item):
         category = item.category
         if category not in self.items_dic:
            self.items_dic[category] = []
         self.items_dic[category].append(item) 

    def removeItem(self, item):
         category = item.category
         if category in self.items_dic:
              for each_item in self.items_dic[category]:
                   if each_item.upc == item.upc:
                        self.items_dic[category].remove(each_item)
                        return
    
    def removeCategory(self, category):
            category = category.upper()
            if category in self.items_dic:
                del self.items_dic[category]

    def getItems(self, category):
        category = category.upper()
        if category not in self.items_dic:
            return ""

        result = ""
        for index, item in enumerate(self.items_dic[category]):
            if index > 0:
                result += "\n"
            result += item.toString()

        return result 

    def doesItemExist(self, item):
        for item_list in self.items_dic.values():
            for each_item in item_list:
                if each_item.upc == item.upc:
                    return True
        return False
    
    def countDollarItems(self):
        count = 0
        for item_list in self.items_dic.values():
            for each_item in item_list:
                if each_item.price < 1.00:
                    count += 1
        return count
                   
                   


