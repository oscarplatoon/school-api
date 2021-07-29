def course_list(request):
    courses = Course.objects.all()
    serialized_courses=CourseSerializer(courses).all_courses
    return JsonResponse(serialized_courses, status=200)


def course_detail(request, course_id):
    course= get_course(course_id)
    serialized_course=CourseSerializer(course).course_detail
    return JsonResponse(serialized_course, status=200)


def new_course(request):
    if request.method == 'POST':
        data = json.load(request)
        form = courseForm(data)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course=CourseSerializer(course).course_detail
            return(JsonResponse(data=serialized_course, status=200))


def edit_course(request, course_id):
    course = get_course(course_id)
    if request.method == 'POST':
        data = json.load(request)
        form = courseForm(data, instance=course)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course=CourseSerializer(course).course_detail
            return(JsonResponse(data=serialized_course, status=200))

def delete_course(request, course_id):
    if request.method == "POST":
        course=get_course(course_id)
        course.delete()
        return(JsonResponse(data={'status':'Successfully Deleted course'}, status=200))