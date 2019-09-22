{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>ชนิดข้อมูลลิสต์ (List)</h1>\n",
    "<p><strong>List</strong><br>\n",
    "    <pre> เป็นตัวแปรที่มีขึ้นในโปรแกรมภาษาใหม่ ๆ ซึ่งโปรแกรมภาษารุ่นเก่า ๆ จะเรียกว่า อะเรย์ (array) ซึ่งประกอบด้วยตัวแปร 1 ตัว มีข้อมูลเก็บได้หลาย ๆ จำนวนในลักษณะที่ต่อเนื่องกัน การเรียกใช้ข้อมูลภายในลิสต์จะต้องระบุถึงดัชนีลำดับของข้อมูลที่เก็บเอาไว้ โดยเริ่มต้นจาก 0 เช่นเดียวกับอะเรย์ แต่ลิสต์สามารถเรียกดัชนีที่เป็นค่าลบได้ นั่นคือ ถ้าเป็น -1 หมายถึง ข้อมูลลำดับสุดท้าย</pre>\n",
    "</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่างที่ 5.1 การประกาศตัวแปรชนิดข้อมูลลิสต์"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\"]\n",
    "numbers_lst = [1, 2, 3, 4, 5, 6]\n",
    "book_num_lst = [1, \"Python\", 2, \"Java\", 3 ,\"C\", 4, \"C++\", 5, \"C#\"]\n",
    "print(\"รายชื่อหนังสือใน books_lst = \", books_lst)\n",
    "print(\"ตัวเลขใน numbers_lst =\", numbers_lst)\n",
    "print(\"สมาชิกใน book_num_lst =\", book_num_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2><strong>การเข้าถึงตำแหน่งข้อมูลของชนิดข้อมูลลิสต์</strong></h2><br>\n",
    "<pre>เราสามารถเข้าถึงตำแหน่งข้อมูลที่เก็บอยู่ภายในชนิดข้อมูลลิสต์ได้สองทางคือ ทางด้านหน้าและจากทางด้านท้าย ด้วยการระบุตำแหน่ง (index) หากเข้าข้อมูลจากด้านหน้าเริ่มนับจากตำแหน่งที่ 0 ถ้าเข้าจากด้านท้ายจะเริ่มที่ -1 ดังนี้</pre>\n",
    "\n",
    "<table >\n",
    "    <tr>\n",
    "        <td>ตำแหน่งท้าย</td>\n",
    "        <td style=\"text-align: center\">-3</td>\n",
    "        <td style=\"text-align: center\">-2</td>\n",
    "        <td style=\"text-align: center\">-1</td>\n",
    "    <tr>\n",
    "    <tr >\n",
    "        <td>book_list</td>\n",
    "        <td style=\"padding: 10px;border: 1px solid black;text-align: center\">Python</td>\n",
    "        <td style=\"padding: 10px;border: 1px solid black;text-align: center\">C++</td>\n",
    "        <td style=\"padding: 10px;border: 1px solid black;text-align: center\">C</td>\n",
    "    <tr>\n",
    "    <tr>\n",
    "        <td>ตำแหน่งหน้า</td>\n",
    "        <td style=\"text-align: center\">0</td>\n",
    "        <td style=\"text-align: center\">1</td>\n",
    "        <td style=\"text-align: center\">2</td>\n",
    "    <tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่างที่ 5.2 การเขียนคำสั่งโปรแกรมระบุตำแหน่งแสดงข้อมูลที่เก็บอยู่ในชนิดข้อมุลลิสต์"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\", \"PHP\", \".NET\" ]\n",
    "print (\"ตำแหน่ง -5 ใน books_lst คือ\", books_lst[-5])\n",
    "print (\"ตำแหน่ง 1-6 ใน books_lst คือ\", books_lst[:6])\n",
    "print (\"ตำแหน่ง 1-4 ใน books_lst คือ\", books_lst[1:4])\n",
    "print (\"แสดงข้อมูลจากตำแหน่งที่ 1-6 โดยข้ามที่ละ 2 = \", books_lst[1:6:2])\n",
    "print (\"แสดงข้อมูลทั้งหมดใน books_lst โดยข้ามที่ละ 2 = \", books_lst[::2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>เมธอดที่ใช้กับข้อมูลลิสต์</h1>\n",
    "<h3>1.append()</h3>\n",
    "<p>ใช้สำหรับเพิ่มข้อมูลต่อท้ายลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> lst.append(x)</td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์\n",
    "    x คือ ข้อมูลใหม่ที่ต้องการเพิ่ม\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.3 การเขียนคำสั่งโปรแกรมเพิ่มข้อมูล โดยใช้เมธอด append()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = ['Python', 'Java', 'C', 'C++', 'C#' ]\n",
    "books_lst.append(\"Scala\")\n",
    "print (\"แสดงรายการหนังสือใน books_lst = \", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>2.clear()</h3>\n",
    "<p>ใช้สำหรับลบข้อมุลทั้งหมดออกจากลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.clear()\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.4 การเขียนคำสั่งโปรแกรมลบข้อมูลทั้งหมดออกจากลิสต์ โดยใช้เมธอด clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\"]\n",
    "books_lst.clear()\n",
    "print (\"ข้อมูลที่อยู่ใน books_lst =\", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>3.copy()</h3>\n",
    "<p>ใช้สำหรับคัดลองข้อมูลลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst_new = lst.copy()\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์\n",
    "    lst_new คือ ตัวแปรเก็บข้อมูลลิสต์\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.5 การเขียนคำสั่งโปรแกรมคัดลอกชนิดข้อมูลลิสต์ โดยใช้เมธอด copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\"]\n",
    "books_lst1 = books_lst.copy()\n",
    "print (\"ข้อมูลที่อยู่ใน books_lst1 =\", books_lst1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>4.count()</h3>\n",
    "<p>ใช้สำหรับนับจำนวนข้อมูลที่ซ้ำกันในข้อมูลลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.count(x)\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์\n",
    "    x คือ ข้อมูลที่ต้องการนับ\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.6 การเขียนคำสั่งโปรแกรมนับข้อมูลที่ต้องการในลิสต์ โดยใช้เมธอด count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "numbers_lst = [1, 5, 4, 5, 4, 7, 6, 5, 9, 10, 15]\n",
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\", \"Python\" ]\n",
    "print (\"จำนวนเลข 5 ใน numbers_lst =\", numbers_lst.count(5))\n",
    "print (\"จำนวนคำ Python ใน books_lst =\", books_lst.count(\"Python\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>5.extend()</h3>\n",
    "<p>ใช้สำหรับเพิ่มลิสต์เข้าไปในลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.extend(x)\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ ที่ต้องการนำ x มาเพิ่ม\n",
    "    x คือ ข้อมูลลิสต์\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.7 การเขียนคำสั่งโปรแกรมเพิ่มลิสต์ในข้อมูลลิสต์ โดยใช้เมธอด extend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\"]\n",
    "books_lst.extend([4, 5, 8, 9])\n",
    "print(books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>6. index()</h3>\n",
    "<p>ใช้สำหรับค้นหาตำแหน่งข้อมุลที่เก็บอยู่ในลิสต์ ถ้าพบข้อมูลอยู่ในลิสต์จะคืนค่าตำแหน่งกลับมา ถ้าข้อมูลที่ต้องการแสดงตำแหน่งไม่มีอยู่ในลิสต์ จะคืนค่ากลับมาเป็นการแจ้งเตือนข้อผิดพลาด มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.index( x, start, stop )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ ที่ต้องการค้นหาตำแหน่งข้อมูล\n",
    "    x คือ ข้อมูลลิสต์ที่ต้องการค้าหาตำแหน่ง\n",
    "    start คือ จุดเริ่มต้นที่ต้องการให้ค้าหาตำแหน่ง\n",
    "    stop คือ จุดสิ้นสุดที่ต้องการให้ค้าหาตำแหน่ง\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.8 การเขียนคำสั่งโปรแกรมค้าหาตำแหน่งข้อมูลในลิสต์ โดยใช้เมธอด index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"PHP\", \"Scala\"]\n",
    "numbers_lst = [1, 50, 4, 51, 4, -17.45, 6, 0.5, -1.459, 10, 15]\n",
    "print (\"ตำแหน่งหนังสือภาษา C ใน books_lst =\", books_lst.index(\"C\", 0, 6))\n",
    "print (\"ตำแหน่งตัวเลข 0.5 ใน numbers_lst =\", numbers_lst.index(0.5, 2, 8))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>7. insert()</h3>\n",
    "<p>ใช้สำหรับแทรกข้อมูลเข้าไปในลิสต์ โดยระบุตำแหน่ง มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.insert( index, x )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ ที่ต้องการแทรกข้อมูล\n",
    "    index คือ ตำแหน่งที่ต้องการแทรกข้อมูล\n",
    "    x คือ ข้อมูลที่ต้องการแทรก\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.9 การเขียนคำสั่งโปรแกรมแทรกข้อมูลในลิสต์ โดยใช้เมธอด insert()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\"]\n",
    "books_lst.insert(4,\".NET\")\n",
    "books_lst.insert(2,\"PHP\")\n",
    "print(\"จำนวนรายการหนังสือใหม่ =\", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>8. pop()</h3>\n",
    "<p>ใช้สำหรับลบข้อมูลบข้อมูลในลิสต์ โดยระบุตำแหน่ง มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.pop( index )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ \n",
    "    index คือ ตำแหน่งที่ต้องการลบข้อมูล\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.10 การเขียนคำสั่งโปรแกรมลบข้อมูลออกจากลิสต์ โดยใช้เมธอด pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\" ]\n",
    "books_lst.pop()\n",
    "books_lst.pop(2)\n",
    "print(\"จำนวนรายการหนังสือใน books_lst = \", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>9. remove()</h3>\n",
    "<p>ใช้สำหรับลบข้อมูลบข้อมูลด้วยการระบุชื่อ ถ้าไม่มีข้อมูลที่ระบุไว้จะคืนค่ากลับมาเป็นการแจ้งเตือนข้อผิดพลาด มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.remove( x )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ \n",
    "    x คือ ข้อมูลที่ต้องการลบออกจากลิสต์\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.11 การเขียนคำสั่งโปรแกรมลบข้อมูลโดยการระบุชื่อ โดยใช้เมธอด remove()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\"]\n",
    "books_lst.remove(\"C#\")\n",
    "print (\"จำนวนหนังสือในลิสต์ books_lst =\", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่าง ทดสอบเมื่อไม่มีข้อมูลในลิสต์"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\"]\n",
    "books_lst.remove(\"PHP\")\n",
    "print (\"จำนวนหนังสือในลิสต์ books_lst =\", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>10. reverse()</h3>\n",
    "<p>ใช้สำหรับสลับตำแหน่งข้อมูลจากด้านหลังมาด้านหน้า มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.reverse( x )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ \n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.12 การเขียนคำสั่งโปรแกรมสลับตำแหน่งข้อมูลจากด้านหลังมาด้านหน้า โดยใช้เมธอด reverse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\"]\n",
    "books_lst.reverse()\n",
    "print(\"เรียงลำดับหนังสือใหม่ใน books_lst =\", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>11. sort()</h3>\n",
    "<p>ใช้สำหรับเรียงลำดับข้อมูลที่อยู่ในลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                lst.sort(  )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ \n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.13 การเขียนคำสั่งโปรแกรมเรียงลำดับข้อมูลที่อยู่ในลิสต์ โดยใช้เมธอด sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C++\", \"C#\", \"Scala\" ]\n",
    "books_lst.sort()\n",
    "print(\"เรียงรายการหนังสือใน books_lst ใหม่ = \", books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>12. len()</h3>\n",
    "<p>ใช้สำหรับแสดงจำนวนข้อมูลที่อยู่ในลิสต์ มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> \n",
    "                len( lst )\n",
    "            </td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    lst คือ ตัวแปรชนิดข้อมูลลิสต์ \n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.14 การเขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลที่อยู่ในลิสต์ โดยใช้เมธอด len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"C\"]\n",
    "numbers_lst = [5, 10, -15, -20.45, 60, 48, 46.12]\n",
    "print(\"จำนวนรายการหนังสือทั้งหมดใน books_lst คือ \", len(books_lst))\n",
    "print(\"จำนวนตัวเลขทั้งหมดใน number_lst คือ \", len(numbers_lst))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>การดำเนินการกับชนิดข้อมูลลิสต์</h2>\n",
    "<pre>เราสามารถดำเนินการต่างๆ กับลิสต์ เช่น การทำซ้ำลิสต์ การเชื่อมลิสต์เข้าด้วยกัน การเปรียบเทียบลิสต์ การค้นหาสมาชิกในลิสต์ ดังตัวอย่างต่อไปนี้</pre>\n",
    "\n",
    "ตัวอย่างที่ 5.20 การเขียนคำสั่งโปรแกรมการดำเนินการต่างๆ กับลิสต์"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nums_lst = [4, 5, 4.12, 7, -5.12, 15]\n",
    "nums_lst1 = [4, 3, 5, -9, -45, 78]\n",
    "books_lst = [\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"Scala\" ]\n",
    "print (nums_lst + books_lst)\n",
    "print (nums_lst * 3)\n",
    "print (\"เปรียบเทียบ num_lst กับ nums_lst1 เท่ากันหรือไม่ = \", nums_lst == nums_lst1)\n",
    "news_lst = [nums_lst, books_lst]\n",
    "print (news_lst)\n",
    "print (\"ค้นหาหนังสือภาษา Python ใน books_list =\", \"Python\" in books_lst)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่างที่ 5.21 การเขียนคำสั่งโปรแกรมเรียกใช้ฟังก์ชัน min(), max(), sum() กับข้อมูลลิสต์"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "numbers_lst = [1, 5.5, 4, 5, 4.12, 7.8, 6, -5.12, 9.46, -10, 15]\n",
    "print(\"ค่าที่น้อยที่สุดใน numbers_lst = \", min(numbers_lst))\n",
    "print(\"ค่าที่มากที่สุดใน numbers_lst = \", max(numbers_lst))\n",
    "print(\"ผลรวมของ numbers_lst = \", sum(numbers_lst))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>แบบฝึกหัด</h2>\n",
    "<p><pre>\n",
    "1.กำหนดให้ month = [\"Jan\", \"May\", \"Jul\", \"Aug\", \"Oct\", \"Dec\"]<br>\n",
    "1.1 ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด แทรกเดือนที่ขาดหายไป\n",
    "1.2 ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด ลบชื่อเดือนตำแน่งที่ 2, 5, 9 ออกจากลิสต์\n",
    "1.3 ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอด แสดงชื่อเดือนที่เหลืออยู่ในลิสต์<br>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "แทรกเดือนที่ขาดหายไป = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']\n",
      "ลบชื่อเดือนตำแหน่งที่ 2,5,9 ออกจากลิสต์ = ['Jan', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Oct', 'Nov', 'Dec']\n",
      "แสดงชื่อเดือนที่เหลืออยู่ในลิสต์ = ['Jan', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Oct', 'Nov', 'Dec']\n"
     ]
    }
   ],
   "source": [
    "month=[\"Jan\",\"May\",\"Jul\",\"Aug\",\"Oct\",\"Dec\"]\n",
    "month.insert(1,\"Feb\")\n",
    "month.insert(2,\"Mar\")\n",
    "month.insert(3,\"Apr\")\n",
    "month.insert(5,\"Jun\")\n",
    "month.insert(8,\"Sep\")\n",
    "month.insert(10,\"Nov\")\n",
    "print(\"แทรกเดือนที่ขาดหายไป =\",month)\n",
    "month.remove(\"Feb\")\n",
    "month.remove(\"May\")\n",
    "month.remove(\"Sep\")\n",
    "print(\"ลบชื่อเดือนตำแหน่งที่ 2,5,9 ออกจากลิสต์ =\",month)\n",
    "print(\"แสดงชื่อเดือนที่เหลืออยู่ในลิสต์ =\",month)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.กำหนดให้ days = [\"Sun\", \"Mon\", \"Tue\", \"Wed\", \"Thu\", \"Fri\", \"Sat\"]<br>\n",
    "2.1 ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอดเรียงชื่อวันจากท้ายสุด\n",
    "2.2 ให้เขียนคำสั่งโปรแกรมเรียกใช้เมธอดเรียงลำดับชื่อวันตามตัวอักษร\n",
    "2.3 ให้เขียนคำสั่งโปรแกรมแสดงชื่อวัน ในตำแหน่งที่ 3, 5 และ 7</pre>\n",
    "</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "เรียงชื่อวันจากท้ายสุด = ['Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon', 'Sun']\n",
      "เรียงลำดับชื่อวันตามตัวอักษร = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']\n",
      "แสดงชื่อวันมรตำแหน่งที่ 3,5 และ 7 = ['Sat', 'Thu', 'Wed']\n"
     ]
    }
   ],
   "source": [
    "days = [\"Sun\",\"Mon\",\"Tue\",\"Wed\",\"Thu\",\"Fri\",\"Sat\"]\n",
    "days.reverse()\n",
    "print(\"เรียงชื่อวันจากท้ายสุด =\",days)\n",
    "days.sort()\n",
    "print(\"เรียงลำดับชื่อวันตามตัวอักษร =\",day)\n",
    "print(\"แสดงชื่อวันมรตำแหน่งที่ 3,5 และ 7 =\",days[2:7:2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
