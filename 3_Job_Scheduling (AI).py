# Jobs, Profit, Slot
profit = [15,27,10,100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 
profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
slot = []
for _ in range(len(jobs)):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)):
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        #check if slot is occupied
        for j in range(job[2], 0, -1):
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Jobs scheduled buddy:",ans[1:])
print(profit)

'''✅ Title:
Job Sequencing with Deadlines using Greedy Algorithm

✅ Algorithm (Step-by-step):
Input: List of jobs with their respective profits and deadlines.

Combine the jobs with profit and deadline using zip().

Sort all jobs in decreasing order of profit.

Initialize:

A slot array (0 = empty, 1 = filled).

An answer array to store job order.

For each job (highest profit first):

Try to assign it to the latest available time slot before its deadline.

If a slot is free, assign the job and mark the slot as filled.

Print the scheduled jobs and total profit.

✅ Python Code Output:
less
Copy
Edit
Jobs scheduled buddy: ['j5', 'j4', 'j2', 'j1']
292
✅ Features / Key Points:
Greedy algorithm.

Maximizes total profit while meeting job deadlines.

Efficient for small to medium-sized job sets.

✅ Time and Space Complexity:
Time Complexity: O(n²)
(due to nested loop: sorting + checking slots)

Space Complexity: O(n)

✅ Data Structures Used:
List → to track slots and scheduled jobs.

Tuple/List of Tuples → to pair jobs with profit and deadline.

✅ Short Theory:
The Job Sequencing Problem is a classic greedy algorithm problem where we are given a set of jobs with deadlines and associated profits. The goal is to schedule the jobs in a way that maximizes total profit without violating any deadlines — only one job can be scheduled at a time.

✅ Viva Questions with Answers:
Q1: What is the Job Sequencing Problem?
A1: It is a scheduling problem where we aim to maximize profit by scheduling jobs within their deadlines.

Q2: Which algorithm is used here?
A2: Greedy Algorithm.

Q3: What is the time complexity?
A3: O(n²), where n is the number of jobs.

Q4: Can more than one job be scheduled in a single slot?
A4: No, each time slot can contain only one job.

Q5: Why are the jobs sorted by profit?
A5: To ensure the most profitable jobs are scheduled first — greedily maximizing profit.

Q6: How do we check for a free slot?
A6: By iterating from the job's deadline down to 1 and checking the slot array.

Q7: What is the greedy choice in this algorithm?
A7: Choosing the job with the highest profit and trying to schedule it as late as possible before its deadline.

Q8: What happens if all slots are full?
A8: The job is skipped; it cannot be scheduled.

Q9: Can the deadlines be more than the number of jobs?
A9: Yes, but we only create as many slots as jobs since more time than jobs doesn’t increase profit.

Q10: Where is this algorithm practically used?
A10: In resource allocation, project planning, and manufacturing systems where deadlines and profits matter.'''