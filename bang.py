class sinhvien:
	def __init__(self,mssv,hoten,makhoa):
		self.mssv = mssv
		self.hoten = hoten
		self.makhoa = makhoa
	def getmssv(self):
		return self.mssv
	def gethoten(self):
		return self.hoten
	def getmakhoa(self):
		return self.makhoa
	def setmssv(self,mssv):
		self.mssv = mssv
	def sethoten(self,hoten):
		self.hoten = hoten
	def setmssv(self,makhoa):
		 self.makhoa = makhoa
	def toString(self):
		print (self.mssv,"  ",self.hoten,"  ",self.makhoa)
	sv = sinhvien("001" ,"Mai A","01")
	sv.toString()
	sv1 = sinhvien("002" ,"Tran B","01")
	sv1.toString()
	sv2 = sinhvien("003" ,"Van C","02")
	sv2.toString()
	sv3 = sinhvien("004" ,"Thi K","01")
	sv3.toString()
class khoa:
	def __init__(self,makhoa,tenkhoa):
		self.makhoa = makhoa
		self.tenkhoa = tenkhoa
	def getmakhoa(self):
		return self.makhoa
	def gettenkhoa(self):
		return self.tenkhoa
	def setmakhoa(self,makhoa):
		self.makhoa = makhoa
	def settenkhoa(self,tenkhoa):
		self.tenkhoa = tenkhoa
	def toString(self):
		print (self.makhoa,"  ",self.tenkhoa)
	k = khoa("01","CNTT")
	k.toString()
	k1 = khoa("02","Ke Toan")
	k1.toString()
  	k2 = khoa("03","Co Khi")
	k2.toString()

	

	
	



	

