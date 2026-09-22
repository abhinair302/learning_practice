data=read.csv("SOCR-HeightWeight.csv")
print(names(data))
model=lm(data$Weight.Pounds~data$Height.Inches,data=data,family=binomial)
print(summary(model))
print(coef(model))
new_data=data.frame(x=108)
result=predict(model,new_data,type="response")
print("Prediction: ")
print(result)
plot(data$Weight.Pounds,data$Height.Inches,
    main="Height vs Weight",
    xlab="Height",
    ylab="Weight",
    pch=10,
    col="red")

abline(model,col="blue")
dev.off()