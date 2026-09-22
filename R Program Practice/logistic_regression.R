data=read.csv("student_data.csv")
print(names(data))

model=glm(Result~Hours,data=data,family=binomial)
print(summary(model))
print(coef(model))
new_data=data.frame(Hours=5)
prediction=predict(model,new_data,type="response")
print("Prediction: ",prediction)

val=ifelse(prediction>=0.5,1,0)
cat(val)
classs=ifelse(val==1,"Pass","Fail")
cat("Result=",classs)
