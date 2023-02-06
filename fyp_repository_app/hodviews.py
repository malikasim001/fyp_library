import os
from django.conf import settings
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render

import nltk
from nltk.util import ngrams
from  nltk.metrics.distance import jaccard_distance

from fyp_repository_app.models import Projects

from fyp_repository_app.models import Departments, CustomUser, Admindep, Supervisor, Student,Projects


def BaseClass(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request,"hod_templates/base_class.html",{"user":user})

def AddAdmin(request):
    departments=Departments.objects.all()
    return render(request, "hod_templates/addadmin.html",{"departments":departments})

def Admin_Save(request):
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
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        dep_id = request.POST.get("dep_id")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  last_name=last_name, first_name=first_name, user_type=3)
            user.admindep.address = address
            user.admindep.gender = gender
            user.admindep.office_location = office_loc
            user.admindep.profile_pic = profile_pic_url
            dep_obj = Departments.objects.get(id=dep_id)
            user.admindep.dep_id = dep_obj
            user.save()
            return HttpResponseRedirect("/add_admin")

        except:
            return HttpResponse("Failed to add Admin")

def Manage_Admin(request):
    admins=Admindep.objects.all()
    return render(request, "hod_templates/manage_admin.html",{"adminss":admins})

def Edit_Admin(request,admin_id):
    departments=Departments.objects.all()
    admins=Admindep.objects.get(admin=admin_id)
    return render(request, "hod_templates/edit_admin.html", {"admins": admins, "departments":departments})

def Edit_admin_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        admin_id=request.POST.get("admin_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        office_loc = request.POST.get("office_loc")
        dep_id = request.POST.get("dep_id")
        #if request.FILES['profile_pic']:
        if request.FILES.get('profile_pic',False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=admin_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            admin = Admindep.objects.get(admin=admin_id)
            admin.address = address
            admin.gender = gender
            admin.office_location=office_loc
            department=Departments.objects.get(id=dep_id)
            admin.dep_id=department
            if profile_pic_url != None:
                admin.profile_pic = profile_pic_url

            admin.save()
            return HttpResponseRedirect("/add_admin")

        except:
            return HttpResponse("Failed to update Admin")

def AddStudent(request):
    departments=Departments.objects.all()
    supervisors=CustomUser.objects.filter(user_type='2')
    return render(request, "hod_templates/addstudent.html",{"departments":departments, "supervisors":supervisors})

def Add_Student_Save(request):
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
            return HttpResponseRedirect("/addstudent")
        except:
            return HttpResponse("Failed to add student")
def Manage_Student(request):
    students = Student.objects.all()
    return render(request, "hod_templates/manage_student.html", {"students": students})
def Edit_Student(request,student_id):
    departments = Departments.objects.all()
    students = Student.objects.get(admin=student_id)
    return render(request, "hod_templates/edit_student.html", {"students": students, "departments": departments})

def Edit_Student_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        student_id=request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        cgpa = request.POST.get("cgpa")
        dep_id = request.POST.get("dep_id")
        #if request.FILES['profile_pic']:
        if request.FILES.get('profile_pic',False):
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
            return HttpResponseRedirect("/manage_student")

        except:
            return HttpResponse("Failed to update Student Record")

def AddSupervisor(request):
    departments=Departments.objects.all()
    return render(request,"hod_templates/add_supervisor.html",{"departments":departments})

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
        gender=request.POST.get("gender")
        office_loc=request.POST.get("office_loc")
        designation=request.POST.get("designation")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        dep_id = request.POST.get("dep_id")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.supervisor.address = address
            user.supervisor.gender=gender
            user.supervisor.office_location=office_loc
            user.supervisor.designation=designation
            user.supervisor.profile_pic = profile_pic_url
            dep_obj = Departments.objects.get(id=dep_id)
            user.supervisor.dep_id = dep_obj
            user.save()
            return HttpResponseRedirect("/addsupervisor")
        except:
            return HttpResponse("Failed to add SuperVisor")

def Manage_Supervisor(request):
    supervisors = Supervisor.objects.all()
    return render(request, "hod_templates/manage_supervisor.html", {"supervisorss": supervisors})

def Edit_Supervisor(request,supervisor_id):
    departments = Departments.objects.all()
    supervisor = Supervisor.objects.get(admin=supervisor_id)
    return render(request, "hod_templates/edit_supervisor.html", {"admins": supervisor, "departments": departments})

def Edit_Supervisor_Save(request):
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
            return HttpResponseRedirect("/manage_supervisor")

        except:
            return HttpResponse("Failed to update Supervisor")


def AddDepartment(request):
    return render(request, "hod_templates/add_department.html")

def Department_Save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        try:
            dep_id = request.POST.get("department_id")
            department_model=Departments(name=dep_id)
            department_model.save()
            return HttpResponseRedirect("/adddepartment")
        except:
            return HttpResponse("Failed to Add Department")
def Manage_Department(request):
    departments=Departments.objects.all()
    return render(request,"hod_templates/manage_department.html",{"departments":departments})

def Edit_Department(request,department_id):
    department=Departments.objects.get(id=department_id)
    return render(request, "hod_templates/edit_department.html", {"department": department})

def Edit_Department_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        dep_id = request.POST.get("dep_id")
        dep_name = request.POST.get("dep_name")
        try:
            departments=Departments.objects.get(id=dep_id)
            departments.name=dep_name
            departments.save()
            return HttpResponseRedirect("/manage_department")

        except:
            return HttpResponse("Failed to update Department")

def Add_Fyp(request):
    departments=Departments.objects.all()
    supervisors=CustomUser.objects.filter(user_type=2)
    return render(request, "hod_templates/add_fyp.html", {"departments":departments, "supervisors":supervisors})


def Fyp_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("pro_title")
        year = request.POST.get("year")
        sup_id=request.POST.get("sup_id")
        dep_id=request.POST.get("dep_id")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        try:
            department_model = Projects(title=title,year=year,dep_id_id=dep_id,admin_id=sup_id,report_file=profile_pic_url)
            department_model.save()
            return HttpResponseRedirect("/add_fyp")
        # p=Projects.objects.get(title=title)
        # return HttpResponse(department_model)
        except:
            return HttpResponse("FAILED TO ADD FYP")

def Show_Project(request):
    project=Projects.objects.all()
    return render(request,"hod_templates/past_fyp.html",{"project":project})

def PastFyp(request):
    project = Projects.objects.all()
    return render(request, "hod_templates/past_fyp.html",{"projects":project})

def CurrentFyp(request):
    return render(request, "hod_templates/current_fyp.html")

def UploadReport(request):
    return render(request, "hod_templates/upload_report.html")

def LogOut(request):
    logout(request)
    return HttpResponseRedirect("/")

def Show_Profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request, "hod_templates/show_profile.html", {"user":user})

def Downloadd(request,pathh):
    file_path=os.path.join(settings.MEDIA_ROOT, os.path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/report_file")
            response['content-Disposition']='inline:filename='+os.path.basename(file_path)
            return response
    raise Http404

def UploadReport(request):
    return render(request, "hod_templates/upload_report.html")

def N_Gram(request):
    import os
    import nltk
    import numpy as np
    import math
    import docx
    from nltk.corpus import stopwords
    # doc file input in python
    project = Projects.objects.all()
    report = request.FILES['report']
    def getText(filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)

    # input filepath where all assignment belong
    docFiles = []
    docFiles1=[]
    for filename in os.listdir("D:\\fyp_repository_system\\fyp_repository_systems\media"):
        if filename.endswith('.docx'):
            filename = getText(filename)
            filename1=getText(report)
            docFiles.append(filename)#files from media folder
            docFiles1.append(filename1)#file which is uploaded from student
    docFiles.sort(key=str.lower)
    docFiles1.sort(key=str.lower)
    print(len(docFiles))
    print(len(docFiles1))
    # building vocabulary of a the documents

    def build_lexicon(corpus):
        lexicon = set()
        for doc in corpus:
            # word tokenization
            word_token = [word for word in doc.split()]
            lower_word_list = [i.lower() for i in word_token]

            # stemming
            porter = nltk.PorterStemmer()
            stemmed_word = [porter.stem(t) for t in lower_word_list]

            # removing stop words
            stop_words = set(stopwords.words('english'))
            filtered_bag_of_word = [w for w in stemmed_word if not w in stop_words]
            lexicon.update(filtered_bag_of_word)
        return lexicon

    # all word set
    vocabulary = build_lexicon(docFiles)
    vocabulary1 = build_lexicon(docFiles1)
    def tf(term, document):
        return freq(term, document)

    def freq(term, document):
        return document.split().count(term)

    doc_term_matrix = []
    print('\n Our Vocabulary vector is [' + ','.join(list(vocabulary)) + ']')
    print('\n Our Vocabulary vector is [' + ','.join(list(vocabulary1)) + ']')
    for doc in docFiles:
        tf_vector = [tf(word, doc) for word in vocabulary]
        tf_vector_string = ','.join(format(freq, 'd') for freq in tf_vector)
        print('\n the tf vector for document %d is [%s]' % ((docFiles.index(doc) + 1), tf_vector_string))
        doc_term_matrix.append(tf_vector)
    print('\n ll combined here is our master document term matrix:')
    print(doc_term_matrix)
    doc1_term_matrix = []
    for doc in docFiles1:
        tf_vector = [tf(word, doc) for word in vocabulary1]
        tf_vector_string = ','.join(format(freq, 'd') for freq in tf_vector)
        print('\n the tf vector for document %d is [%s]' % ((docFiles1.index(doc) + 1), tf_vector_string))
        doc1_term_matrix.append(tf_vector)

    print('\n ll combined here is our master document term matrix:')
    print(doc1_term_matrix)
    #return HttpResponse(doc1_term_matrix)

    # Now every document is in the same feature space
    # Normalizing vectors to l2 norm
    # l2 norm of each vector is 1

    def l2_normalizer(vec):
        denom = np.sum([e1 ** 2 for e1 in vec])
        return [(e1 / math.sqrt(denom)) for e1 in vec]

    doc_term_martix_l2 = []
    doc1_term_martix_l2 = []
    for vec in doc_term_matrix:
        doc_term_martix_l2.append(l2_normalizer(vec))

    for vec in doc1_term_matrix:
        doc1_term_martix_l2.append(l2_normalizer(vec))
    print('\nA regular old document term martix:  ')
    print(np.matrix(doc_term_matrix))
    print(np.matrix(doc1_term_matrix))
    print('\nA document term matrix with row wise l2 norms of 1:  ')
    print(np.matrix(doc_term_martix_l2))
    print(np.matrix(doc1_term_martix_l2))

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
    my_idf_vector1 = [idf(word, docFiles1) for word in vocabulary1]
    print('our vocabuary vector is[ ' + ','.join(list(vocabulary1)) + ']')

    print('\nThe inverse document frequency vectir is [' + ','.join(format(freq('f') for freq in my_idf_vector)))
    print('\nThe inverse document frequency vectir is [' + ','.join(format(freq('f') for freq in my_idf_vector1)))
    #return HttpResponse(my_idf_vector1)
    def build_idf_matrix(idf_vector):
        idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
        np.fill_diagonal(idf_mat, idf_vector)
        return idf_mat

    my_idf_matrix = build_idf_matrix(my_idf_vector)
    print('\nIdf matrix is:')
    print(my_idf_matrix)
    my_idf_matrix1 = build_idf_matrix(my_idf_vector1)
    print('\nIdf matrix is:')
    print(my_idf_matrix1)

    doc_term_matrix_tfidf = []
    doc1_term_matrix_tfidf = []
    # performing tfidf matrix multiplication
       #is jaga kuch changing krni pry gi be in mind for report file matrix
    for tf_vector in doc_term_matrix:
        doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))
        #return HttpResponse(doc_term_matrix_tfidf)
    for tf_vector in doc1_term_matrix:
        doc1_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix1))
        #return HttpResponse(doc_term_matrix_tfidf)
    # normalising
    doc_term_matrix_tfidf_l2 = []
    doc1_term_matrix_tfidf_l2 = []
    for tf_vector in doc_term_matrix_tfidf:
        doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))
    print(vocabulary)
    print(np.matrix(doc_term_matrix_tfidf_l2))
    for tf_vector in doc1_term_matrix_tfidf:
        doc1_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))
    print(vocabulary)
    print(np.matrix(doc1_term_matrix_tfidf_l2))
    #return HttpResponse(np.matrix(doc1_term_matrix_tfidf_l2))
    # cosine distance and angle between all the documents pairwisely
    for i in range(len(docFiles1)):
        for j in range(len(docFiles)):
            result_nltk = nltk.cluster.util.cosine_distance(doc1_term_matrix_tfidf_l2[i], doc_term_matrix_tfidf_l2[j])
            return HttpResponse("HELLO")
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