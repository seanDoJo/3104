import matplotlib.pyplot as plt
import mySortingFunctions

insertData = []
mergeData = []
qsortData = []
insertWorst = []
mergeWorst = []
qsortWorst = []

xcords = []
z = -1
for i in range(5, 505, 5):
	xcords.append(i)

for i in range(5, 505, 5):
	insertMid = []
	mergeMid = []
	qsortMid = []
	z += 1
	insertWorst.append(0)
	mergeWorst.append(0)
	qsortWorst.append(0)
	for x in range(0, 1001):
		randList = mySortingFunctions.generateRandomList(i)

		insertTime = mySortingFunctions.measureRunningTimeComplexity(mySortingFunctions.insertionSort, randList)
		if (insertTime > insertWorst[z]):
			insertWorst[z] = insertTime
		mergeTime = mySortingFunctions.measureRunningTimeComplexity(mySortingFunctions.mergeSort, randList)
		if (mergeTime > mergeWorst[z]):
			mergeWorst[z] = mergeTime
		qsortTime = mySortingFunctions.measureRunningTimeComplexity(mySortingFunctions.quickSort, randList)
		if (qsortTime > qsortWorst[z]):
			qsortWorst[z] = insertTime

		insertMid.append(insertTime)
		mergeMid.append(mergeTime)
		qsortMid.append(qsortTime)

	
	insertAvg = 0
	mergeAvg = 0
	qsortAvg = 0

	for j in range(0, 1001):
		insertAvg += insertMid[j]
		mergeAvg += mergeMid[j]
		qsortAvg += qsortMid[j]


	insertAvg = insertAvg / 1001
	mergeAvg = mergeAvg / 1001
	qsortAvg = qsortAvg / 1001

	insertData.append(insertAvg)
	mergeData.append(mergeAvg)
	qsortData.append(qsortAvg)

fig, ax1 = plt.subplots()
ax1.plot(xcords, insertData, 'r--', label='Average Case')
plt.ylim([0, 0.006])
ax1.set_xlabel('Array Size')
ax1.set_ylabel('Time to Sort')

ax2 = ax1.twinx()
ax2.plot(xcords, insertWorst, 'b--', label='Worst Case')
plt.xlim([0, 510])
plt.ylim([0, 0.006])
plt.title('Average and Worst Case Insertion Sort')
legend = ax1.legend(loc='upper right', shadow='true')
legend2 = ax2.legend(loc='lower right', shadow='true')
plt.savefig('insertionSortMixedResults.png', bbox_inches='tight')
plt.clf()

fig, ax1 = plt.subplots()
ax1.plot(xcords, mergeData, 'r--', label='Average Case')
plt.ylim([0, 0.004])
ax1.set_xlabel('Array Size')
ax1.set_ylabel('Time to Sort')

ax2 = ax1.twinx()
ax2.plot(xcords, mergeWorst, 'b--', label='Worst Case')
plt.xlim([0, 510])
plt.ylim([0, 0.004])
plt.title('Average and Worst Case Merge Sort')
legend = ax1.legend(loc='upper right', shadow='true')
legend2 = ax2.legend(loc='lower right', shadow='true')
plt.savefig('mergeSortMixedResults.png', bbox_inches='tight')
plt.clf()

fig, ax1 = plt.subplots()
ax1.plot(xcords, qsortData, 'r--', label='Average Case')
plt.ylim([0, 0.004])
ax1.set_xlabel('Array Size')
ax1.set_ylabel('Time to Sort')

ax2 = ax1.twinx()
ax2.plot(xcords, qsortWorst, 'b--', label='Worst Case')
plt.xlim([0, 510])
plt.ylim([0, 0.004])
plt.title('Average and Worst Case Quick Sort')
legend = ax1.legend(loc='upper right', shadow='true')
legend2 = ax2.legend(loc='lower right', shadow='true')
plt.savefig('quickSortMixedResults.png', bbox_inches='tight')
plt.clf()
