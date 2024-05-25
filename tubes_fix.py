import streamlit as st
import time

def brute_force(guessed_digit, true_digit):

    if guessed_digit != true_digit :
        return guessed_digit+1, False
    else :
        return guessed_digit, True

def divide_and_conquer(guessed_digit, true_digit, left, right):
    list_prob_int = list(range(10000))

    mid = (left + right) // 2

    if true_digit > list_prob_int[mid]:
        left = mid + 1
    elif true_digit < list_prob_int[mid] :
        right = mid - 1
    elif true_digit == guessed_digit :
        return mid, True, mid, mid
    
    mid = (left + right) // 2

    return mid, False, left, right
    



st.title("Tugas Besar SA")
st.write("Harits Arkaan Putranto - 1301223438")
st.write("Rangga Aldora Permadi - 1301223425")
st.write("Ulayya Azizna - 1301220091")
st.write("Enter the correct code")
text = st.empty()
error_message = st.empty()
input_placeholder = st.empty()

# Initial input
input_user = input_placeholder.text_input("Correct Code")

# Validation loop
while True:
    if not input_user.isdigit() and input_user != '':
        error_message.error("Inputan harus berupa angka")
    elif len(input_user) != 4 and input_user != '':
        error_message.error("Inputan harus terdiri dari 4 digit")
    elif input_user == '' :
        error_message.empty()
    else:
        error_message.empty()  # Clear any previous error message
        break

true_digit = int(input_user)

col1, col2 = st.columns(2)
with col1 :
    guessing_brute = st.empty()
    brute_iterasi = st.empty()
    time_brute = st.empty()
with col2 :
    guessing_div = st.empty()
    div_iterasi = st.empty()
    time_div = st.empty()

left, right = 0, 9999
brute_status, div_status = False, False
guessed_brute, guessed_div = 0, 0
i, j = 0, 0

start_time_brute = time.time()
start_time_div = time.time()
while not brute_status or not div_status :
    guessing_brute.write(f'Brute Force         : {guessed_brute:04d}')
    guessing_div.write(f'Divide & Conquer    : {guessed_div:04d}')

    brute_iterasi.write(f'Iterasi ke-{j}')
    div_iterasi.write(f'Iterasi ke-{i}')

    if div_status == False:
        end_time_div = time.time()
        div_duration = end_time_div - start_time_div

    if brute_status == False:
        end_time_brute = time.time()
        brute_duration = end_time_brute - start_time_brute
    
    time_brute.write(f'Waktu: {brute_duration:.2f} detik')
    time_div.write(f'Waktu: {div_duration:.2f} detik')

    guessed_brute, brute_status = brute_force(guessed_brute, true_digit)
    guessed_div, div_status, left, right = divide_and_conquer(guessed_div, true_digit, left, right)
    
    if div_status == False:
        i +=1

    if brute_status == False:
        j +=1
    
    time.sleep(0.1)