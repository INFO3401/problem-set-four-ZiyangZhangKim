# Ziyang Zhang, Yizhen Wu, and Talia Colalancia
# Problem 1
# Problem 2
# pip install realclearpolitics
# rcp https://www.realclearpolitics.com/epolls/2020/president/us/2020_democratic_presidential_nomination-6730.html
# Problem 3 & 4
from utils import *
from poll import *
import math
from candidate import Candidate
import seaborn as sns
import matplotlib.pyplot as plt
#df = loadAndCleanData("endorsements-2020.csv")
#print(df)
candidateNames = pd.unique(endorsements['endorsee'])
print(candidateNames)
candidates = {}
val = {}
# problem 5
def normalizeData(df):
	x = df.copy()
	sumList = []

	for i, row in x.iterrows():
		row.drop(labels=["Poll","Data","Sample","Spread"],inplace=True)
		print(row)
		sumList.append(100-sum(row))
	x["Undecided"]=sumList
	print(x)
# Problem 6
normalizeData(df)
# print(plotCandidate)
# Problem 7
def plotCandidate(Candidate, df):
	plt.scatter(y=df[candidate],x=df["Poll"]) # variables no quotes
	plt.title(candidate + " Polling")
	plt.ylim(0) # bottom is 0
	plt.show()

for candidate in df.columns:
	if candidate not in ["Poll","Data","Sample","Spread","Undecided"]:
		plotCandidate(candidate,df)
# Problem 8
def statsPerCandidate(candidate, df):
	return df[candidate].mean()

# Problem 9
myCandidate = []
for candidate in df.columns:
	if candidate not in ["Poll","Data","Sample","Spread","Undecided"]:
		myCandidate.append(candidate)
		print(candidate.statsPerCandidate(candidate,df))
	# print(statsPerCandidate)
# Problem 10
def cleanSample(df):
	sampleType = []
	sampleSize = []

	for i in df["Sample"]:
		sampleType.append(i[-2:])
		sampleSize.append(i[-2:])

	df["Sample Type"] = sampleType
	df["Sample Size"] = sampleSize
	return df
# Problem 11
test = cleanSample(df)
print(cleanSample)
# Problem 12
def computePollWeight(df,poll):
	x = df["Poll"] == poll
	xSum = sum(x["Sample Size"])
	y = sum(df["Sample Size"])
	return xSum/y
# Problem 13
def weightStatsPerCandidate(candidate,df):
	weightAverages = []
	for poll in df["Poll"].unique():
		x = sum(df[df["Poll"] == poll][candidate])
		y = computePollWeight(df,poll)
	weightAverages.append(x*y)
	return sum(weightAverages)/len(weightAverages)
# Problem 14
weightStatsPerCandidate("Biden",df)
weightStatsPerCandidate("Warren",df)
weightStatsPerCandidate("Sanders",df)
# Problem 15
def computeCorrelation(candidate1,candidate2,df):
	return df[candidate1].corr(df[candidate2])
# Problem 16
repeatList = []
for candidate in myCandidate:
	for candidate2 in myCandidate:
		if candidate1 != candidate2:
			if [candidate1,candidate2] not in repeatList:
				print(candidate1+" vs "+candidate2+": "+computeCorrelation(candidate1,candidate2,df))
				repeatList.append([candidate1,candidate2])
# Problem 17
def superTuesday(df,candidates):
	BidenST = []
	SandersST = []

	for i, row in df.iterrows():
		BidenCount = row['Biden']
		SandersCount = row["Sanders"]
		for candidate in candidates:
			if candidate != "Biden" and candidate != "Sanders":
				BidenCorr = computeCorrelation("Biden",candidate,df)
				SandersCorr = computeCorrelation("Sanders",candidate,df)
				if abs(BidenCorr) > abs(SandersCorr):
					BidenCount += row[candidate]
				else:
					SandersCount += row[candidate]

			BidenST.append(BidenCount)
			SandersST.append(SandersCount)
			df["BidenST"] = BidenST
			df["SandersST"] = SandersST

# Problem 18
superTuesday(df,myCandidate)
print("Biden Mean: "+df["BidenST"].mean())
print("Sanders Mean: "+df["SandersST"].mean())
print("Biden Weighted Mean: "+weightStatsPerCandidate("BidenST",df))
print("Sanders Weighted Mean: "+weightStatsPerCandidate("SandersST",df))

# Problem 19
getConfidenceInterval(df["BidenST"])
getConfidenceInterval(df["SandersST"])

# Problem 20
print("Numbers: "+runTTest(df["Biden"],df["Sanders"]))
print("Aggregated Numbers: "+runTTest(df["BidenST"],df["SandersST"]))

# Problem 21
df = loadAndCleanData("Post-Super Tuesday.csv")


# Problem 22



