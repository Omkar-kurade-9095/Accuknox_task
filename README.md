Question_1_Answer= yes Django signals are executed synchronously. I have creted task 1 for that .you have the run the "python manage.py test_signal_sync" in terminal 
you can observe 5 secondas delay that is called inside signal handler this demonstrates that the caller waits for the signal to finish before continuing


output= PS E:\Django\task_completion> python manage.py test_signal_sync
            [Caller] Creating instance...
            [Signal] Signal triggered for instance: Original Name
            [Signal] Simulating long task...
            [Signal] Signal processing completed
            [Caller] Instance created: Original Name
            [Caller] Total time taken: 5.01 seconds

Question_2_answer= Yes, by default, Django signals run in the same thread as the caller. To demonstrate this, we can capture the thread information in both the caller and the signal handler using Python’s threading module
If the thread IDs match, it will prove that the signal is executed in the same thread as the caller
run "python manage.py test_signal_thread1" in terminal


output=PS E:\Django\task_completion> python manage.py test_signal_thread1
          [Caller] Creating instance in thread: MainThread (Thread ID: 14320)
          [Signal] Signal triggered for instance: Original Name    
          [Signal] Running in thread: MainThread (Thread ID: 14320)
          [Caller] Instance created: Original Name

Question_3_answer= Yes, by default, Django signals run in the same database transaction as the caller. This means that any database changes made in the signal handler are part of the same transaction as the caller's.
If the caller's transaction is rolled back, the signal's changes are also rolled back
run "python manage.py test_signal_transaction" in terminal

output= [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Signal] Signal triggered. Updating status for instance: Test Object
        [Caller] Exception occurred: maximum recursion depth exceeded
        [Caller] Total instances in DB after rollback: 0

