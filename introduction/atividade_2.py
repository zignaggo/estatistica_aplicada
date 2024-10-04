import scipy.stats as stats
from main import sync1, asyncr1

LIMIT = 0.05
normality_sync1 = stats.shapiro(sync1)
normality_asyncr1 = stats.shapiro(asyncr1)

if normality_sync1.pvalue < LIMIT:
    print("rejeitar h0: ", normality_sync1.pvalue)
print("não rejeitar h0: ", normality_sync1.pvalue)
if normality_asyncr1.pvalue < LIMIT:
    print("rejeitar h0: ", normality_asyncr1.pvalue)
print("não rejeitar h0: ", normality_asyncr1.pvalue)