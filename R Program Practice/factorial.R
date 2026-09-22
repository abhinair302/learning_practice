fact<-function(n){
    if (n==1 || n==0){
        return(1)
    } else{
        return(n*fact(n-1))
    }
}

cat("Enter a number: ")
n=readLines(con="stdin",n=1)
n<-as.numeric(n)
print(n)
result<-fact(n)
cat("The factorial of",n,"is: ",result)
