from django.shortcuts import render

from app.models import *

from django.db.models import Q
# Create your views here.

def equijoins(request):
    EMPOBJECTS=Employee.objects.select_related('deptno').all()
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(sal__gt=2000)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(job='SALESMAN')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__dlocation='BOSTAN')
    EMPOBJECTS=Employee.objects.select_related('deptno').all()
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(hiredate__year=2022)
    EMPOBJECTS=Employee.objects.select_related('deptno').all(job='ANALYST')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(Ename='ALLEN')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__Ename='KING')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(Ename='ALLEN',mgr__Ename='')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__Ename='JONES')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__Ename='KING')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(sal__gte=2500)
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    EMPMGROBJECTS=Employee.objects.select_related('mgr').all()
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(Ename='ALLEN')
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__Ename='KING')
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(Ename='ALLEN',mgr__Ename='')
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__Ename='JONES')
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__Ename='KING')
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(sal__gte=2500)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(sal__lte=2000,comm__isnull=True)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(sal__lte=1000,mgr__sal__gte=3000)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__Ename='BLAKE',sal__lte=1300,comm__gte=800)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__deptno=30,)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__deptno=10,hiredate__year=2022,sal__gte=100)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(comm__isnull=False)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(comm__isnull=False,comm__gt=800)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(sal__lt=1650)
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(mgr__Ename='BLAKE')
    EMPMGROBJECTS=Employee.objects.select_related('mgr').filter(job='SALESMAN')
    
    d={'EMPMGROBJECTS':EMPMGROBJECTS}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Employee.objects.select_related('deptno','mgr').all()
    emd=Employee.objects.select_related('deptno','mgr').filter(Ename='JONES')
    emd=Employee.objects.select_related('deptno','mgr').filter(sal__gt=2000)
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno=20,sal__lte=960)
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emd=Employee.objects.select_related('deptno','mgr').filter(hiredate__year=2023,hiredate__month=4)
    emd=Employee.objects.select_related('deptno','mgr').filter(Ename__startswith='M')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__Ename__startswith='B')
    emd=Employee.objects.select_related('deptno','mgr').filter(hiredate__year__gt=2022,hiredate__year__lt=2024)
    emd=Employee.objects.select_related('deptno','mgr').all()[:5:]
    emd=Employee.objects.select_related('deptno','mgr').filter(job='CLERK',deptno__dname='ACCOUNTING')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__job='MANAGER')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__job='MANAGER')[3:6:]
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(mgr__job='ANALYST')|Q(job='SALESMAN',sal__gte=2000))
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__Ename__contains='A')
    emd=Employee.objects.select_related('deptno','mgr').filter(job__contains='MAN')
    emd=Employee.objects.select_related('deptno','mgr').filter(job__startswith='MAN')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__in=(10,30))
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(deptno=30)|Q(mgr__Ename='BLAKE'))
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__in=(10,30))
    emd=Employee.objects.select_related('deptno','mgr').filter(Ename__in=('BLAKE','ALLEN','JONES'))
    emd=Employee.objects.select_related('deptno','mgr').filter(sal__lte=1500,mgr__deptno__in=(10,20))
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno=20,deptno__dname='RESEARCH')
    emd=Employee.objects.select_related('deptno','mgr').filter(sal__lte=1000,mgr__sal__gte=3000)
    emd=Employee.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__deptno=10,hiredate__year=2022,sal__gte=100)
    emd=Employee.objects.select_related('deptno','mgr').filter(comm__isnull=False,comm__gt=800)
    emd=Employee.objects.select_related('deptno','mgr').filter(Ename='ALLEN',mgr__Ename='')
    emd=Employee.objects.select_related('deptno','mgr').filter(sal__lte=2000,comm__isnull=True)
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__Ename='BLAKE',sal__lte=1300,comm__gte=800)
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__in=(10,20))[2:4:]
    emd=Employee.objects.select_related('deptno','mgr').filter(Ename='ALLEN',sal__gte=2000)
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(mgr__Ename='JONES')|Q(Ename='SMITH'))
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dlocation__in=('NEW YORK','CHICAGO'))





    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)