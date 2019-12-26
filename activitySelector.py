def selectionSort(start, finish, activities):
	for i in range(len(finish)):
		min_index = i
		for j in range(i + 1, len(finish)):
			if finish[min_index] > finish[j]:
				min_index = j


		start[i], start[min_index] = start[min_index], start[i]
		finish[i], finish[min_index] = finish[min_index], finish[i]
		activities[i], activities[min_index] = activities[min_index], activities[i]

	return start, finish, activities


def activitySelector(start, finish, activities):
	selected = [activities[0]]
	last = finish[0]
	for i in range(1, len(start)):
		if start[i] >= last:
			selected.append(activities[i])
			last = finish[i]
	return selected


def activitySelectorRecursive(start, finish, activities):
	selected = activities[:1]
	end = finish[0]
	i = 1
	while i < len(activities) and start[i] < end:
		i += 1

	if i < len(activities):
		return selected + activitySelectorRecursive(start[i:], finish[i:], activities[i:])
	return selected

if __name__ == '__main__':
    start = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish = [10, 11, 6, 9, 9, 7, 10, 11, 12, 13, 14]
    activities = list(range(0, len(start)))
    start, finish, activities = selectionSort(start, finish, activities)
    print(activitySelectorRecursive(start, finish, activities))
    print(activitySelector(start, finish, activities))
