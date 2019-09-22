{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>ชนิดข้อมูลทูเพิล (Tuple)</h1>\n",
    "<p><strong>Tuple</strong><br>\n",
    "    <pre>ตัวแปรชนิดทุพเพิล เป็นตัวแปรที่มีลักษณะคล้ายกับตัวแปรชนิดลิสต์ เพียงแต่ตัวแปรชนิดทุพเพิลไม่สามารถนำมาเพิ่มเติมหรือเปลี่ยนแปลงข้อมูลได้เลยเมื่อได้สร้างขึ้นมาแล้ว ดังนั้น การเรียกใช้ข้อมูลจึงมีการใช้ตัวเลขดัชนีเช่นเดียวกัน และที่แตกต่างกันอีกอย่างหนึ่งคือ ในขณะสร้างตัวแปร ตัวแปรชนิดทุพเพิลจะมีข้อมูลอยู่ภายใต้เครื่องหมาย ‘()’ ในขณะที่ตัวแปรชนิดลิสต์จะมีข้อมูลอยู่ภายใต้เครื่องหมาย ‘[]’</pre>\n",
    "</p>\n",
    "\n",
    "ตัวอย่างที่ 5.15 การเขียนคำสั่งโปรแกรมสร้างตัวแปรชนิดข้อมูลทูเพิลขึ้นมาใช้งาน"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tup = ()\n",
    "vars_tup = (\"Name\", \"Address\", [1, 2, 3], (\"ID\", 3451))\n",
    "book_tup = (\"Python Programming\")\n",
    "book_tup1 = (\"Python Programming\",)\n",
    "print (vars_tup)\n",
    "print (\"ชนิดข้อมูลของ vars_tup คือ\", type(vars_tup))\n",
    "print (\"ชนิดข้อมูลของ book_tup คือ\", type(book_tup))\n",
    "print (\"ชนิดข้อมูลของ book_tup1 คือ\", type(book_tup1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่างที่ 5.16 การแจ้งเตือนข้อผิดพลาดเมื่อใช้เมธอด remove() และ insert()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_tup = (\"Python\", \"Java\", \"C\", \"C++\", \"C#\")\n",
    "books_tup.remove(\"Python\")\n",
    "print(\"จำนวนหนังสือในรายการ = \", books_tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_tup = (\"Python\", \"Java\", \"C\", \"C++\", \"C#\")\n",
    "books_tup.insert(3, \".NET\")\n",
    "print(\"จำนวนหนังสือในรายการ = \", books_tup)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>เมธอดที่ใช้กับข้อมูลทูเพิล</h1>\n",
    "<h3>1.index()</h3>\n",
    "<p>ใช้สำหรับแสดงตำแหน่งข้อมูล มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> tup.index(x)</td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    tup คือ ตัวแปรชนิดข้อมูลทูเพิล\n",
    "    x คือ ข้อมูลที่ต้องการตำแหน่ง\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.17 การเขียนคำสั่งโปรแกรมแสดงตำแหน่งข้อมูลในทูเพิล ด้วยเมธอด index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_tup = (\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"PHP\")\n",
    "numbers_tup = (5, 10, -15, -20.45, 60, 48, 46.12)\n",
    "print(\"ตำแหน่งของหนังสือภาษา Python คือ \", books_tup.index(\"Python\"))\n",
    "print(\"ตำแหน่งเลข -20.45 คือ \", numbers_tup.index(-20.45, 0,5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>2.count()</h3>\n",
    "<p>ใช้สำหรับนับจำนวนข้อมูลที่เก็บอยู่ในตัวแปรชนิดทูเพิล มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> tup.count(x)</td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    tup คือ ตัวแปรชนิดข้อมูลทูเพิล\n",
    "    x คือ ข้อมูลที่ต้องการนับ\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.18 การเขียนคำสั่งโปรแกรมนับจำนวนข้อมูลที่เก็บอยู่ในตัวแปรชนิดทูเพิล ด้วยเมธอด count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_tup = (\"Python\", \"C\", \"C++\", \"Java\", \"Python\", \"PHP\", \"C\", \"Java\")\n",
    "numbers_tup = (45, 5, 10, 45, -15, -20.45, 45, 60, 48, 45, 46.12, 45)\n",
    "print(\"จำนวนหนังสือภาษา Python ทั้งหมด คือ\", books_tup.count(\"Python\"), \"เล่ม\")\n",
    "print(\"จำนวนตัวเลข 45 ทั้งหมด คือ\", numbers_tup.count(45), \"ตัว\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>3.len()</h3>\n",
    "<p>ใช้สำหรับสำหรับแสดงจำนวนข้อมูลทั้งหมดที่เก็บอยู่ในชนิดข้อมูลทูเพิล มีรูปแบบดังนี้</p>\n",
    "    <table>\n",
    "        <tr>\n",
    "            <td style=\"padding: 10px;border: 1px solid black;text-align: center\"> len(tup)</td>\n",
    "        </tr>\n",
    "    </table>\n",
    "    <pre>โดยที่\n",
    "    tup คือ ตัวแปรชนิดข้อมูลทูเพิล\n",
    "    </pre>\n",
    "    ตัวอย่างที่ 5.19 การเขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดที่เก็บอยู่ในชนิดข้อมูลทูเพิล ด้วยเมธอด len()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_tup = (\"Python\", \"Java\", \"C\", \"C++\", \"C#\", \"C\")\n",
    "numbers_tup = (5, 10, -15, -20.45, 60, 48, 46.12)\n",
    "print(\"จำนวนหนังสือทั้งหมด คือ\",len(books_tup), \"เล่ม\")\n",
    "print(\"จำนวนตัวเลขทั้งหมด คือ\", len(numbers_tup), \"ตัว\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>การดำเนินการกับชนิดข้อมูลทูเพิล</h2>\n",
    "<pre>เราสามารถดำเนินการต่างๆ กับทูเพิลได้เหมือนกับ ลิสต์ เช่น การเปรียบเทียบ การหาค่าสูงสุด การค่าต่ำสุด การหาค่าผลรวม การทำซ้ำ เป็นต้น ดังตัวอย่างต่อไปนี้</pre>\n",
    "\n",
    "ตัวอย่างที่ 5.22 การเขียนคำสั่งโปรแกรมและตรวจสอบการเป็นสมาชิกในชนิดข้อมูลทูเพิล"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "books_tup = (\"Python\", \"Java\", \"C\", \"C++\", \"C#\")\n",
    "print(\"มีหนังสือ .Net หรือไม่ = \", \".Net\" in books_tup)\n",
    "print(\"มีหนังสือ C# หรือไม่ = \", \"C#\" in books_tup)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่างที่ 5.23 การเขียนคำสั่งโปรแกรมหาค่าต่ำสุด ค่าสูงสุด และผลรวม จากชนิดทูเพิล"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "numbers_tup = (4, 5, 4.12, 7, -5.12, -10, 15)\n",
    "print (\"ค่าสูงสุดใน numbers_tup คือ\", max(numbers_tup))\n",
    "print (\"ค่าสูงต่ำใน numbers_tup คือ\", min(numbers_tup))\n",
    "print (\"ผลรวมของ numbers_tup คือ\", sum(numbers_tup))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ตัวอย่างที่ 5.24 การเปรียบเทียบ การเชื่อม การทำซ้ำ ชนิดข้อมูลทูเพิล"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "num_tup_1 = (4, 5, 7, -5.12, -10, 15)\n",
    "num_tup_2 = (4, 5, 4.12, 7,)\n",
    "num_tup_3 = (4, 5, 4.12, 7,)\n",
    "books_tup_1 = (\"Python\", \"Java\", \"C\", \"C++\", \"C#\")\n",
    "books_tup_2 = (\"C\", \"C++\", \"C#\")\n",
    "less_than = num_tup_1 < num_tup_3\n",
    "equal_ = num_tup_2 == num_tup_3\n",
    "merge = books_tup_1 + books_tup_2\n",
    "dup = books_tup_1 * 2\n",
    "print (\"ผลเปรียบเทียบ num_tup_1 < num_tuple_3 คือ\", less_than)\n",
    "print (\"ผลเปรียบเทียบ num_tup_1 = num_tuple_3 คือ\",  equal_)\n",
    "print (\"ผลการวมระหว่าง books_tup_1 กับ books_tuple_2 คือ\",  merge)\n",
    "print (\"ผลการคูณของ books_tup_1 คือ\", dup)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>แบบฝึกหัด</h2>\n",
    "<p><pre>\n",
    "1.กำหนดให้ brand_cars = (\"Toyota\", \"Honda\", \"Benz\", \"BMW\", \"Tesla\", \"Ford\", \"KIA\", \"Volvo\" )<br>\n",
    "1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของ Benz, Ford และ Volvo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ตำแหน่งของ Benz คือ 2\n",
      "ตำแหน่งของ Ford คือ 5\n",
      "ตำแหน่งของ Volvo คือ 7\n",
      "จำนวนข้อมูลทั้งหมดในทูเพิล คือ 8 รายการ\n",
      "มียี่ห้อรถ Suzuki อยู่ใน brand_cars หรือไม่ = False\n",
      "มียี่ห้อรถ Ferrari อยู่ใน brand_cars หรือไม่ = False\n",
      "มียี่ห้อรถ Ford อยู่ใน brand_cars หรือไม่ = True\n"
     ]
    }
   ],
   "source": [
    "brand_cars =(\"Toyota\",\"Honda\",\"Benz\",\"BMW\",\"Tesla\",\"Ford\",\"KIA\",\"Volvo\")\n",
    "print(\"ตำแหน่งของ Benz คือ\",brand_cars.index(\"Benz\"))\n",
    "print(\"ตำแหน่งของ Ford คือ\",brand_cars.index(\"Ford\"))\n",
    "print(\"ตำแหน่งของ Volvo คือ\",brand_cars.index(\"Volvo\"))\n",
    "print(\"จำนวนข้อมูลทั้งหมดในทูเพิล คือ\",len(brand_cars),\"รายการ\")\n",
    "print(\"มียี่ห้อรถ Suzuki อยู่ใน brand_cars หรือไม่ =\",\"Suzuki\"in brand_cars)\n",
    "print(\"มียี่ห้อรถ Ferrari อยู่ใน brand_cars หรือไม่ =\",\"Ferrari\"in brand_cars)\n",
    "print(\"มียี่ห้อรถ Ford อยู่ใน brand_cars หรือไม่ =\",\"Ford\"in brand_cars)"
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
