设计、编制、调试一个典型的语法分析程序
实现对如下文法的递归子程序语法分析

本分析程序所分析的文法如下：
G[E]：
	E→eBaA
	A→a|bAcB
	B→dEd|aC
	C→e|dC
