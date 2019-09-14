#!/usr/bin/env python
# coding: utf-8

# # 1. 

# In[60]:


จำนวนเงิน=float(input("จำนวนเงิน:"))
ภาษี=float(input("ภาษี:"))
เปอร์เซ็นต์=จำนวนเงิน*(ภาษี/100)
print(เปอร์เซ็นต์,"บาท")


# # 2.

# In[58]:


A=float(input("ตัวเลขที่ 1:"))
B=float(input("ตัวเลขที่ 2:"))
if A>B:
    print("ตัวเลขที่ 1 มีค่ามากกว่าตัวเลขที่ 2")
elif A<B:
    print("ตัวเลขที่ 1 มีค่าน้อยกว่าตัวเลขที่ 2")
else:
    print("ตัวเลขทั้งสองมีค่าเท่ากัน")


# # 3.

# In[55]:


x=1
while x<=5:
    print("Hello")
    x=x+1


# # 4.

# In[54]:


x=2
for k in range(1,x+11):
    s=x*k
    print("2 x",k,"=",s)
    

