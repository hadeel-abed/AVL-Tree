#username-abdelhaleem1
#id1     -211758842
#name1   -Hadeel Abdelhaleem
#id2     -211708516
#name2   -Wael Zidan
import copy
import random
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)   
        mergeSort(R)
        i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def rotateLL(node):
        AVLTreeList.rotations+=1
        tmp=node.left
        tmpr=node.left.right
        tmp_cnt_node = tmpr.count + node.right.count + 1
        tmp_cnt = node.left.left.count + tmp_cnt_node + 1
        node.left.right=node
        node.left.right.parent = node.left
        node.left=tmpr
        tmpr.parent = node
        node.height=max(node.left.height,node.right.height)+1
        node.count = tmp_cnt_node
        tmp.count = tmp_cnt
        return tmp

def rotateRR(node):
        AVLTreeList.rotations+=1
        tmp=node.right
        tmpl=node.right.left
        tmp_cnt_node = tmpl.count + node.left.count + 1
        tmp_cnt = node.right.right.count + tmp_cnt_node + 1
        node.right.left=node
        node.right.left.parent = node.right
        node.right=tmpl
        tmpl.parent = node
        node.height=max(node.left.height,node.right.height)+1
        node.count = tmp_cnt_node
        tmp.count = tmp_cnt
        return tmp
def checkandrotate(node):
        if (node.BF()==2):
               
                if(node.left.BF()==-1):
                    node.left=rotateRR(node.left)
                    node=rotateLL(node)
                else:
                    node=rotateLL(node)
        if(node.BF()==-2):
               
                if(node.right.BF()==1):
                    node.right=rotateLL(node.right)
                    node=rotateRR(node)
                else:
                    node=rotateRR(node)
        node.height=max(node.left.height,node.right.height)+1
        return node


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
    """Constructor, you are allowed to add more fields. 

    @type value: str
    @param value: data of your node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.count = 0
        

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """
    
    def insert_aux(node, i, val):
        if node.count == 0:
                node.count = 1
                node.value = val
                node.height = 0
                node.left= AVLNode('virt')
                node.right= AVLNode('virt')
                node.left.parent=node
                node.right.parent=node
                return node
        elif node.left.count >= i-1:
                node.left = node.left.insert_aux(i, val)
        else:
                node.right = node.right.insert_aux(i - node.left.count - 1, val)
        node.count += 1
        node = checkandrotate(node)
        node.left.parent=node
        node.right.parent=node
        return node
    
    def delete_aux(node, i):
        if not node.isRealNode():
                return node
        idx=node.count
        if node.right.isRealNode():
                idx-=node.right.count
        if idx < i:
            node.right = node.right.delete_aux(i - node.left.count - 1)
            node.right.parent = node
            node.count -= 1
        elif idx > i:
            node.left = node.left.delete_aux(i)
            node.left.parent = node
            node.count -= 1
        elif node.right.isRealNode() and node.left.isRealNode():
            tmp = node.right
            while(tmp.left.isRealNode()):
                tmp = tmp.left
            node.value = tmp.value
            node.right = node.right.delete_aux(1)
            node.count -= 1
        elif node.right.isRealNode():
            node.right.parent = node.parent
            node = node.right
        elif node.left.isRealNode():
            node.left.parent = node.parent
            node = node.left
        else:
            return AVLNode('virt')
        node.height = max(node.left.height, node.right.height) + 1
        return checkandrotate(node)
    
    def retrieve_aux(node, i):
                if node.count == 1 or node.count - node.right.count == i:
                        return node.value
                if node.left.count >= i:
                        return node.left.retrieve_aux(i)
                return node.right.retrieve_aux(i- node.left.count - 1)
        
    
            
            
    
    def getLeft(self):
        return self.left
        

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """
    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """
    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """
    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """
    def getHeight(self):
         return self.height
         
    def getsize(self):
            return self.count

    """sets left child

    @type node: AVLNode
    @param node: a node
    """
    def setLeft(self, node):
        self.left=node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """
    def setRight(self, node):
        self.right=node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """
    def setParent(self, node):
        self.parent=node

    """sets value

    @type value: str
    @param value: data
    """
    def setValue(self, value):
        self.value=value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """
    def setHeight(self, h):
        self.height=h

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def isRealNode(self):
        return self.count != 0

    def BF(self):
        return self.left.height - self.right.height
        
        
    def search_aux(node,val):
        if node.count==0: return 0
        if node.value==val: return node.left.count+1
        l=node.left.search_aux(val)
        if l!=0:
                return l
        else:
                r=node.right.search_aux(val)
                if r==0: return 0
                return node.left.count + 1 + node.right.search_aux(val)
        
          

        

"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

    """
    Constructor, you are allowed to add more fields.  

    """
    rotations = 0
    def __init__(self):
        self.root = None
        self.rishon=None
        self.ahron=None


    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """
    def empty(self):
        return self.root == None or self.root.count == 0


    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """
    def retrieve(self, i):
        return self.root.retrieve_aux(i+1)

                

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def insert(self, i, val):
        if i==0:
            self.rishon=val
            if self.length()==0:
                self.ahron=val
        elif i==self.length():
            self.ahron=val
        if self.root is None:
            self.root = AVLNode(val)
            self.root.count = 1
            self.root.height = 0
            self.root.left = AVLNode('virt')
            self.root.right = AVLNode('virt')
            return 0
        
        self.root = self.root.insert_aux(i+1, val)
        self.root.parent = None
        ret=AVLTreeList.rotations
        AVLTreeList.rotations=0
        return ret

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def delete(self, i):
        if i==0:
            if self.length()==1:
                self.rishon=None
                self.ahron=None
            if self.length()==2:
                self.rishon= self.retrieve(1)
                self.ahron=self.retrieve(1)
            else :
                self.rishon=self.retrieve(1)
        if self.length()==2 and i==1:
            self.ahron=self.rishon
        if i==self.root.getsize()-1:
            self.ahron=self.retrieve(self.root.getsize()-2)
        AVLTreeList.rotations=0
        self.root = self.root.delete_aux(i+1)
        return AVLTreeList.rotations


    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """
    def first(self):
        if self.root is None or self.root.getsize()==0:
                return None
        return self.rishon

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """
    def last(self):
        if self.root is None or self.root.getsize()==0:
                return None
        return self.ahron

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """
    def listToArray(self):
        arr = []
        v = self.root
        i = 0
        #fill the list recursively 
        self.listToArrayRec(i, arr, v)
        
        return arr
    def listToArrayRec(self, i, arr, v):
        if (v is not None and v.isRealNode()):
            i = self.listToArrayRec(i, arr, v.getLeft())
            i = i+1
            arr.insert(i, v.getValue())
            i = self.listToArrayRec(i, arr, v.getRight())
        return i

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """
    def length(self):
        if self.root==None: return 0
        return self.root.getsize()
    """sort the info values of the list
    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """
    def sort(self):
        tree= AVLTreeList()
        arr= self.listToArray()
        mergeSort(arr)
        for i in range(len(arr)):
            tree.insert(i,arr[i])
    
       
    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """
    def permutation(self):
        arr=self.listToArray()
        for i in range(0,len(arr)):
            x=random.randint(0, len(arr))
            tmp=arr[i]
            arr[i]=arr[x]
            arr[x]=tmp
        tree=AVLTreeList()
        for i in range(0,len(arr)):
            tree.insert(i, arr[i])
        return tree
    
    """concatenate` lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def concat(self, lst):
        if lst.root is not None:
            self.ahron=lst.ahron
        if self.root == None and lst.root == None:
            return 0
        if self.root == None:
            self.root = lst.root
            self.rishon = lst.rishon
            self.ahron=lst.ahron
            return lst.root.height + 1
        if lst.root == None:
            return self.root.height + 1
        leftHeight = self.root.height
        rightHeight = lst.root.height
        #if we want to maintain lst as is we should deepcopy
        #lst = copy.deepcopy(lst)
        if leftHeight < rightHeight:
            val = self.retrieve(self.root.count-1)
            self.delete(self.root.count-1)
            tmpNode = AVLNode(val)
            tmpNode.count = 1
            tmpNodeII = lst.root
            while tmpNodeII.height > leftHeight:
                tmpNodeII = tmpNodeII.left
            tmpNode.left = self.root
            tmpNode.right = tmpNodeII
            if tmpNodeII.parent is not None:
                tmpNodeII.parent.left = tmpNode
            tmpNode.parent = tmpNodeII.parent
            tmpNodeII.parent = tmpNode
            self.root.parent = tmpNode
            self.root = lst.root
            tmpNode.count = tmpNode.left.count + tmpNode.right.count + 1
            tmpNode.height = max(tmpNode.left.height, tmpNode.right.height)+1
            while tmpNode.parent is not None:
                parent = tmpNode.parent
                parent.left = checkandrotate(tmpNode)
                parent.left.parent = parent
                tmpNode = parent
                tmpNode.count = tmpNode.left.count + tmpNode.right.count + 1
            self.root = checkandrotate(tmpNode)
            self.root.parent = None
        else:
            val = lst.retrieve(0)
            lst.delete(0)
            tmpNode = AVLNode(val)
            tmpNodeII = self.root
            while tmpNodeII.height > rightHeight:
                tmpNodeII = tmpNodeII.right
            tmpNode.right = lst.root
            tmpNode.left = tmpNodeII
            if tmpNodeII.parent is not None:
                tmpNodeII.parent.right = tmpNode
            tmpNode.parent = tmpNodeII.parent
            tmpNodeII.parent = tmpNode
            lst.root.parent = tmpNode
            tmpNode.count = tmpNode.left.count + tmpNode.right.count + 1
            tmpNode.height = max(tmpNode.left.height, tmpNode.right.height)+1
            while tmpNode.parent is not None:
                parent = tmpNode.parent
                parent.right = checkandrotate(tmpNode)
                parent.right.parent = parent
                tmpNode = parent
                tmpNode.count = tmpNode.left.count + tmpNode.right.count + 1
            self.root = checkandrotate(tmpNode)
            self.root.parent = None
        return abs(leftHeight - rightHeight)
            

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """
    def search(self, val):
        if self.root is None:
            return -1
        return self.root.search_aux(val)-1

    def append(self, val):
        self.insert(self.length(), val)
    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """
    def getRoot(self):
        return self.root

    def __str__(self):
                return '---\n'+printTree(self.root)+'---\n'
    
def printTree(node, level=0):
        if(node is None or node.count == 0):
                return "   "*level+"virt\n"
        PV ='none'
        if node.parent is not None:
            PV = node.parent.value
        ret = "   "*level+node.value+" h "+str(node.height)+" c "+str(node.count)+" pv "+PV+"\n"
        ret += printTree(node.left, level+1)
        ret += printTree(node.right, level+1)
        return ret


