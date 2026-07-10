## 1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: 3011

OJ submission ID ถ้ามีการส่งแล้ว: 543164

สถานะ OJ: Pass 

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 minutes

## 2. ความเข้าใจโจทย์ของฉัน
จากโจทย์ต้องการให้เขียนโปรแกรมผสมสี โดยที่มี input เป็นชื่อสี (Red Yellow และ Blue) และต้องการให้ output ออกมาเป็นชื่อสีที่ผสมได้ (Orange Violet และ Green)

## 3. แผนแรกของฉัน
สร้าง input 2 ตัว รับค่าของสีทั้ง 2 สีแล้วเชคว่าสีมาจากที่กำหนดไหม ถ้าใช่ก็ให้เข้าการผสม ถ้าไม่ใช่ก้ error

## 4. วิธีสุดท้ายที่ใช้จริง
สร้างฟังก์ชัน mix สร้าง input 2 ตัวเป็นชื่อสีที่จะผสม set ค่าสี ได้แก่ Red Yellow และ Blue ตั้งค่าตัวแปร fcon = {c1, c2} ให้สีสลับที่กันได้ 
1. ถ้า สีทั้งสองไม่ได้มาจากในตัวเลือกที่ set ไว้ ให้แสดง "Error"
2. นับสี ถ้าซ้ำกันให้แสดงค่าสีนั้น
3. ถ้า สีคือ "Red" และ "Yellow" แสดง "Orange"
4. ถ้า สีคือ "Red" และ "Blue" แสดง "Violet"
5. ถ้า สีคือ "Yellow" และ "Blue" แสดง "Green"
เมื่อครบแล้ว ใช้คำสั่ง mix() เพื่อเรียกใช้ฟังก์ชัน

## 5. การทดสอบของฉัน
### Test Case 1
ทำไมเลือก case นี้: ทดสอบว่ารันโค้ดแล้วได้ค่าตามที่ต้องการไหม

Input: Red
       Yellow

Expected output: Orange

Actual output: Orange

Result: Pass 
### Test Case 2
ทำไมเลือก case นี้: ทดสอบถ้าเป็นสีเดียวกันโปรแกรมจะรันยังไง

Input: Blue
       Blue

Expected output: Blue

Actual output: Blue

Result: Pass 
### Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าถ้าใช้สีที่ไม่ได้ set จะเป็นยังไง

Input: Black
       White

Expected output: Gray

Actual output: Error

Result: Pass 

## 6. การใช้ AI
ใช้ AI กับโจทย์นี้หรือไม่: Yes 

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่: No

## 8. คำรับรองของนักศึกษา

 | Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |

