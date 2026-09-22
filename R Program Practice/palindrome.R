pal<-function(nums){
    new_num=0
    n<-nums
    while(n>0){
        rem=n%%10
        new_num=new_num+(rem*(10^length(n)))
        n=n%/%10
    }
    if (new_num==nums){
        cat("Palindrome\n")
    } else{
        cat("Not Palindrome\n")
    }
}

cat("Enter a number: ")
nums<-readLines(con="stdin",n=1)
nums<-as.integer(nums)
result<-pal(nums)
pal(nums)