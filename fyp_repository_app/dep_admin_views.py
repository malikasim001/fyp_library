from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from fyp_repository_app.models import Departments, CustomUser, Admindep, Supervisor, Student, Projects


def BaseClass(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request,"simple_admin/admin_base_class.html",{"user":user})

def AddSupervisor(request):
    departments = Departments.objects.all()
    return render(request, "simple_admin/add_supervisor.html",{"departments":departments})

def Add_Supervisor_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        office_loc = request.POST.get("office_loc")
        designation = request.POST.get("designation")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        dep_id = request.POST.get("dep_id")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.supervisor.address = address
            user.supervisor.gender = gender
            user.supervisor.office_location = office_loc
            user.supervisor.designation = designation
            user.supervisor.profile_pic = profile_pic_url
            dep_obj = Departments.objects.get(id=dep_id)
            user.supervisor.dep_id = dep_obj
            user.save()
            return HttpResponseRedirect("/add_supervisor")
        except:
            return HttpResponse("Failed to add SuperVisor")

def Manage_Supervisor(request):
    user = CustomUser.objects.get(id=request.user.id)
    depp_id = user.admindep.dep_id
    supervisors = Supervisor.objects.filter(dep_id=depp_id)
    return render(request, "simple_admin/manage_supervisor.html",{"supervisorss":supervisors})
    #return HttpResponse("Hello")

def Edit_Supervisors(request,supervisors_id):
    departments = Departments.objects.all()
    supervisor = Supervisor.objects.get(admin=supervisors_id)
    return render(request, "simple_admin/edit_supervisor.html", {"admins": supervisor,"departments": departments})

def Edit_Save_Supervisors(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        supervisor_id = request.POST.get("supervisor_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        office_loc = request.POST.get("office_loc")
        designation=request.POST.get("designation")
        dep_id = request.POST.get("dep_id")
        # if request.FILES['profile_pic']:
        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=supervisor_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            supervisor = Supervisor.objects.get(admin=supervisor_id)
            supervisor.address = address
            supervisor.gender = gender
            supervisor.office_location = office_loc
            department = Departments.objects.get(id=dep_id)
            supervisor.dep_id = department
            if profile_pic_url != None:
                supervisor.profile_pic = profile_pic_url

            supervisor.save()
            return HttpResponseRedirect("/managee_supervisor")

        except:
            return HttpResponse("Failed to update Supervisor")


def Add_Student(request):
    departments = Departments.objects.all()
    supervisors = CustomUser.objects.filter(user_type='2')
    return render(request, "simple_admin/add_student.html", {"departments": departments, "supervisors": supervisors})

def Add_Student_Savee(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        cgpa=request.POST.get("cgpa")
        gender=request.POST.get("gender")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        dep_id = request.POST.get("dep_id")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  last_name=last_name, first_name=first_name, user_type=4)
            user.student.address=address
            user.student.gender=gender
            user.student.cgpa=cgpa
            user.student.profile_pic = profile_pic_url
            dep_obj = Departments.objects.get(id=dep_id)
            user.student.dep_id = dep_obj
            user.save()
            return HttpResponseRedirect("/add_student")
        except:
            return HttpResponse("Failed to add student")

def Manage_Students(request):
    user=CustomUser.objects.get(id=request.user.id)
    depp_id=user.admindep.dep_id.id
    students=Student.objects.filter(dep_id=depp_id)
    return render(request, "simple_admin/manage_students.html",{"students": students})

def Edit_Students(request,student_id):
    departments = Departments.objects.all()
    students = Student.objects.get(admin=student_id)
    return render(request, "simple_admin/edit_students.html", {"students": students, "departments": departments})

def Edit_Students_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        if request.method != "POST":
            return HttpResponse("Method Not Allowed")
        else:
            student_id = request.POST.get("student_id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            address = request.POST.get("address")
            gender = request.POST.get("gender")
            cgpa = request.POST.get("cgpa")
            dep_id = request.POST.get("dep_id")
            # if request.FILES['profile_pic']:
            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()
                students = Student.objects.get(admin=student_id)
                students.address = address
                students.gender = gender
                students.cgpa = cgpa
                department = Departments.objects.get(id=dep_id)
                students.dep_id = department
                if profile_pic_url != None:
                    students.profile_pic = profile_pic_url
                students.save()
                return HttpResponseRedirect("/manage_students")

            except:
                return HttpResponse("Failed to update Student Record")


def Fyp_Add(request):
    departments = Departments.objects.all()
    supervisors = CustomUser.objects.filter(user_type=2)
    return render(request, "simple_admin/add_fyp.html", {"departments": departments, "supervisors": supervisors})

def Fyp_Savee(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("pro_title")
        year = request.POST.get("year")
        sup_id = request.POST.get("sup_id")
        dep_id = request.POST.get("dep_id")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        try:
            department_model = Projects(title=title, year=year, dep_id_id=dep_id, admin_id=sup_id,
                                        report_file=profile_pic_url)
            department_model.save()
            return HttpResponseRedirect("/fyp_addd")
        # p=Projects.objects.get(title=title)
        # return HttpResponse(department_model)
        except:
            return HttpResponse("FAILED TO ADD FYP")

def Past_Fyp(request):
    project = Projects.objects.all()
    return render(request, "simple_admin/past_fyp.html", {"projects": project})

def Check_plagiarism(request):
    import os
    import nltk
    import numpy as np
    import math
    import docx
    from nltk.corpus import stopwords

    # doc file input in python
    def getText(filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)

    # input filepath where all assignment belong
    docFiles = []
    for filename in os.listdir("D:\\fyp_repository_system\\fyp_repository_systems"):
        if filename.endswith('.docx'):
            filename = getText(filename)
            docFiles.append(filename)
    docFiles.sort(key=str.lower)
    print(len(docFiles))

    # building vocabulary of a  the documents

    def build_lexicon(corpus):
        lexicon = set()
        for doc in corpus:
            # word tokenization
            word_token = [word for word in doc.split()]
            lower_word_list = [i.lower() for i in word_token]

            # stemming removing of COMMA FULLSTOP
            porter = nltk.PorterStemmer()
            stemmed_word = [porter.stem(t) for t in lower_word_list]

            # removing stop words
            stop_words = set(stopwords.words('english'))
            filtered_bag_of_word = [w for w in stemmed_word if not w in stop_words]
            lexicon.update(filtered_bag_of_word)
        return lexicon

    # all word set
    vocabulary = build_lexicon(docFiles)

    def tf(term, document):
        return freq(term, document)

    def freq(term, document):
        return document.split().count(term)

    doc_term_matrix = []
    print('\n Our Vocabulary vector is [' + ','.join(list(vocabulary)) + ']')
    for doc in docFiles:
        tf_vector = [tf(word, doc) for word in vocabulary]
        tf_vector_string = ','.join(format(freq, 'd') for freq in tf_vector)
        print('\n the tf vector for document %d is [%s]' % ((docFiles.index(doc) + 1), tf_vector_string))
        doc_term_matrix.append(tf_vector)

    print('\n ll combined here is our master document term matrix:')
    print(doc_term_matrix)

    # Now every document is in the same feature space
    # Normalizing vectors to l2 norm
    # l2 norm of each vector is 1

    def l2_normalizer(vec):
        denom = np.sum([e1 ** 2 for e1 in vec])
        return [(e1 / math.sqrt(denom)) for e1 in vec]

    doc_term_martix_l2 = []
    for vec in doc_term_matrix:
        doc_term_martix_l2.append(l2_normalizer(vec))

    print('\nA regular old document term martix:  ')
    print(np.matrix(doc_term_matrix))
    print('\nA document term matrix with row wise l2 norms of 1:  ')
    print(np.matrix(doc_term_martix_l2))

    def numDocsContaining(word, doclist):
        doccount = 0
        for doc in doclist:
            if freq(word, doc) > 0:
                doccount = +1
            return doccount

    def idf(word, doclist):
        n_samples = len(doclist)
        df = numDocsContaining(word, doclist)
        return np.log(n_samples / 1 + df)

    my_idf_vector = [idf(word, docFiles) for word in vocabulary]

    print('our vocabuary vector is[ ' + ','.join(list(vocabulary)) + ']')

    print('\nThe inverse document frequency vectir is [' + ','.join(format(freq('f') for freq in my_idf_vector)))

    def build_idf_matrix(idf_vector):
        idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
        np.fill_diagonal(idf_mat, idf_vector)
        return idf_mat

    my_idf_matrix = build_idf_matrix(my_idf_vector)
    print('\nIdf matrix is:')
    print(my_idf_matrix)

    doc_term_matrix_tfidf = []

    # performing tfidf matrix multiplication

    for tf_vector in doc_term_matrix:
        doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))

    # normalising
    doc_term_matrix_tfidf_l2 = []
    for tf_vector in doc_term_matrix_tfidf:
        doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))

    print(vocabulary)
    print(np.matrix(doc_term_matrix_tfidf_l2))

    # cosine distance and angle between all the documents pairwisely
    for i in range(len(docFiles)):
        for j in range(i + 1, len(docFiles)):
            result_nltk = nltk.cluster.util.cosine_distance(doc_term_matrix_tfidf_l2[i], doc_term_matrix_tfidf_l2[j])
            print('\n cosine Distance btw doc %d and doc %d:' % (i, j))
            print(result_nltk)
            cos_sin = 1 - result_nltk
            try:
                angle_in_radians = math.acos(cos_sin)
            except ValueError:
                print("Here Error")
            plagiarism = int(cos_sin * 100)
            print('\nPlagiarism =%s' % plagiarism)
            return HttpResponse(plagiarism)
def Show_Profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request, "simple_admin/profile_admin.html", {"user":user})


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")