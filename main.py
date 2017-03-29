print('press a/A for battleship')
print('press b/B for students becomes teacher')
print('press c/C for exam_stats')

choice = input('enter your choice')
if choice=='a' or choice=='A':
    import battleship
    battleship.battlemain()
elif choice=='b' or choice=='B':
    import students_teacher
    students_teacher.student_teacher_main()
elif choice=='c' or choice=='C':
    import exam_stat
    exam_stat.exam_stats_main()
else:
    print('wrong choice')
