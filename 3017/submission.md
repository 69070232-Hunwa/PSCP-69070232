# บันทึกการแก้โจทย์

## 1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: OJ3017 - Bill

OJ submission ID ถ้ามีการส่งแล้ว: 543166

สถานะ OJ: Pass 

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 minutes

## 2. ความเข้าใจโจทย์ของฉัน
จากโจทย์ต้องการให้เขียนโปรแกรมคำนวนยอดชำระบิล โดยคิด service charge 10% และ vat 7% จากราคาอาหาร

## 3. แผนแรกของฉัน
จากโจทย์ต้องการให้เขียนโปรแกรมคำนวนยอดชำระบิล โดยคิด service charge 10% จากค่าอาหาร ถ้า service charge < 50 บาท จะปัดขึ้นเป็น 50 ถ้า service charge > 1000 บาท จะปัดลงเป็น 1000 แล้วนำมาคิดรวมกับ vat 7%

## 4. วิธีสุดท้ายที่ใช้จริง
สร้างฟังก์ชัน bill สร้าง input รับยอดค่าอาหาร
1. นำค่าอาหาร x 0.1 จะได้ออกมาเป็น service charge
2. ถ้า service charge < 50 บาท จะปัดขึ้นเป็น 50 ถ้า service charge > 1000 บาท จะปัดลงเป็น 1000 
3. นำ service charge ที่ได้ไปรวมกับค่าอาหารตั้งต้น แล้ว x 0.07 
4. แสดงราคาที่ต้องจ่ายทั้งหมดเป็นทศนิยม 2 ตำแหน่ง
เมื่อครบแล้ว ใช้คำสั่ง bill() เพื่อเรียกใช้ฟังก์ชัน

## 5. การทดสอบของฉัน
### Test Case 1
ทำไมเลือก case นี้: กรณีที่ service charge < 50 บาท

Input: 200

Expected output: 267.50

Actual output: 267.50

Result: Pass 
### Test Case 2
ทำไมเลือก case นี้: กรณีที่ service charge > 1000 บาท

Input: 80000

Expected output: 86670.00

Actual output: 86670.00

Result: Pass 
### Test Case 3
ทำไมเลือก case นี้: กรณีที่ service charge อยู่ระหว่าง 50 กับ 1000

Input: 1000

Expected output: 1177.00

Actual output: 1177.00

Result: Pass 

## 6. การใช้ AI
ใช้ AI กับโจทย์นี้หรือไม่: No 

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
