from django.shortcuts import render
#from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse
from .models import User, Account, Bank, Transaction
# Create your views here.
def index(request):
	return render(request,'index.html')
def myacc(request):
	e=request.POST.get('email')
	pwd=request.POST.get('password')
	user=User.objects.filter(email=e)
	if len(user)==0:
		p={'msg':'Please enter registered email id'}
		return render(request,'notfound.html',p)
	else:
		user=user[0]
		if user.password!=pwd:
			p={'msg':'Please enter correct credentials'}
			return render(request,'notfound.html',p)
	a=[]
	x=Account.objects.all()
	for i in x:
		if i.user.email==e:
			a.append(i)
	t=Transaction.objects.all()
	txn=[]
	val=[0,0,0,0,0,0]
	months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
	vm=[0,0,0,0,0,0,0,0,0,0,0,0]
	category=['Food','Gadgets','Transport','Accessories','Clothes','Bills']
	for j in t:
		if j.acc.user.email==e:
			txn.append(j)
			if j.category_name=='food':
				val[0]=val[0]+j.price
			elif j.category_name=='gadgets':
				val[1]=val[1]+j.price
			elif j.category_name=='transport':
				val[2]=val[2]+j.price
			elif j.category_name=='Accessories':
				val[3]=val[3]+j.price
			elif j.category_name=='clothes':
				val[4]=val[4]+j.price
			elif j.category_name=='bills':
				val[5]=val[5]+j.price

			dt=str(j.date)
			dt=dt[5:7]
			print(dt[5:7])
			dtint=int(dt)
			vm[dtint-1]=vm[dtint-1]+j.price

	sumv=sum(vm)
	inc=user.income
	fig3,ax3=plt.subplots()
	ax3.barh(['Yearly Income','Yearly Spending'],[inc,sumv])
	plt.savefig('media/module1/images/barplot2.png')

	fig1,ax1=plt.subplots()
	ax1.pie(val,labels=category,startangle=90)
	ax1.axis('equal')
	ax1.legend()
	plt.savefig('media/module1/images/spending.png',dpi=100)

	fig2,ax2=plt.subplots()
	ax2.bar(months,vm)
	plt.savefig('media/module1/images/barplot.png')

	if (inc-sumv)<=30000:
		msg='1. 70% for living expenses (rent, food, clothing, gasoline)20% for savings 10% for retirement (IRA, 401(k), company pension) 5% for emergencies (car repairs, medical expenses, unemployment) 5% for specific goals (vacation, car, school tuition, a new computer) 10% for debt (student loans, car payments, credit cards)'
		inv='Sinking funds” for future purchases Retirement savings'
	elif (inc-sumv)<=50000:
		msg='50% for living expenses (rent, food, clothing, gasoline)20% for savings 10% for retirement (IRA, 401(k), company pension) 5% for emergencies (car repairs, medical expenses, unemployment) 5% for specific goals (vacation, car, school tuition, a new computer) 10% for debt (student loans, car payments, credit cards)'
		inv='Investment in stocks and bonds'
	else:
		msg='70% for living expenses (rent, food, clothing, gasoline)20% for savings 10% for retirement (IRA, 401(k), company pension) 5% for emergencies (car repairs, medical expenses, unemployment) 5% for specific goals (vacation, car, school tuition, a new computer) 10% for debt (student loans, car payments, credit cards)'
		inv='Seed money to start a business & Investing in real estate'
	param={'user':user,'accounts':a,'txn':txn,'msg':msg,'inv':inv}
	return render(request,'myacc.html',param)

