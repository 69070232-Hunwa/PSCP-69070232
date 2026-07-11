# บันทึกการแก้โจทย์

## 1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: 3025

OJ submission ID ถ้ามีการส่งแล้ว: 549697

สถานะ OJ: Pass 

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 30 minutes

## 2. ความเข้าใจโจทย์ของฉัน
จากโจทย์ต้องการให้แสดงฤดูจากวันที่และเดือน โดยตั้งแต่วันที่ 21 เดือนที่หาร 3 ลงตัวจะนับเป็นฤดูใหม่

## 3. แผนแรกของฉัน
สร้าง input 2 ค่า รับวันที่และเดือน จากนั้นหาเดือนที่หาร 3 ลงตัว ตั้งแต่วันที่ 21

## 4. วิธีสุดท้ายที่ใช้จริง
สร้างฟังก์ชัน season สร้าง input 2 ตัว เป็นวันที่และเดือน ให้เก็บเป็นค่า s
1. ถ้า เดือนเป็น 1, 2, 3 ให้แสดง "winter"
2. ถ้า เดือนเป็น 4, 5, 6 ให้แสดง "spring"
3. ถ้า เดือนเป็น 7, 8, 9 ให้แสดง "summer"
4. ถ้า เดือนเป็น 10, 11, 12 ให้แสดง "fall"

หาเดือนที่หาร 3 ลงตัว ตั้งแต่วันที่ 21 ให้แสดงผลเป็นเดือนถัดไป

1. ถ้า s เป็น "winter" ให้แสดงค่า s ใหม่เป็น "spring"
2. ถ้า s เป็น "spring" ให้แสดง s ใหม่เป็น "summer"
3. ถ้า s เป็น "summer" ให้แสดง s ใหม่เป็น "fall"
4. ถ้า s เป็น "fall" ให้แสดง s ใหม่เป็น "winter"

สุดท้ายแสดงค่า s เมื่อครบแล้ว แล้วใช้คำสั่ง season() เพื่อเรียกใช้ฟังก์ชัน

## 5. การทดสอบของฉัน
### Test Case 1
ทำไมเลือก case นี้: กรณีที่เดือนหาร 3 ไม่ลงตัว

Input: 4 28

Expected output: spring

Actual output: spring

Result: Pass 
### Test Case 2
ทำไมเลือก case นี้: กรณีที่เดือนหาร 3 ลงตัว ตั้งแต่วันที่ 21

Input: 9 25

Expected output: fall

Actual output: fall

Result: Pass 
### Test Case 3
ทำไมเลือก case นี้: กรณีที่เดือนหาร 3 ลงตัว ก่อนวันที่ 21

Input: 3 10

Expected output: winter

Actual output: winter

Result: Pass 

## 6. การใช้ AI
ใช้ AI กับโจทย์นี้หรือไม่: Yes

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ทำร่วมกันกับคู่ pair

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
