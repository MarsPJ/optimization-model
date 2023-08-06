function [flag]=check(x)
    % x1+x2<=15 
    % x3-x4<=0
    % x5=x6
    flag=const1(x)&&const2(x);
end