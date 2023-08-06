%% Matlab自带的粒子群函数 particleswarm
% particleswarm函数是求最小值的
% 如果目标函数是求最大值则需要添加负号从而转换为求最小值。
clear;clc
%% 求解函数y = x1^2+x2^2-x1*x2-10*x1-4*x2+60在[-15,15]内的最小值（最小值为8）
narvs = 2; % 变量个数
% x_lb = [-15 -15]; % x的下界(长度等于变量的个数，每个变量对应一个下界约束)
% x_ub = [15 15]; % x的上界
x_lb = [-3 4.1]; % x的下界(长度等于变量的个数，每个变量对应一个下界约束)
x_ub = [12.1 5.8]; % x的上界
options = optimoptions('particleswarm',...
'PlotFcn','pswplotbestf',...% 绘制最佳的函数值随迭代次数的变化图
'SwarmSize',50,...% 修改粒子数量，默认的是：min(100,10*nvars)
'HybridFcn',@fmincon,... % 在粒子群算法结束后继续调用其他函数进行混合求解
'InertiaRange',[0.2 1.2],... % 惯性权重的变化范围，默认的是0.1-1.1
'SelfAdjustmentWeight',2,...% 个体学习因子，默认的是1.49（压缩因子）
'SocialAdjustmentWeight',2,...% 社会学习因子，默认的是1.49（压缩因子）
'MaxIterations',1000,...% 最大的迭代次数，默认的是200*nvars
'MinNeighborsFraction',0.2,...% 领域内粒子的比例 MinNeighborsFraction，默认是0.25 
'FunctionTolerance',1e-8,...% 函数容忍度FunctionTolerance, 默认1e-6, 用于控制自动退出迭代的参数
'MaxStallIterations',50);% 最大停滞迭代数MaxStallIterations, 默认20, 用于控制自动退出迭代的参数

% 'Display','iter'% 展示函数的迭代过程

tic
[x,fval,exitflag,output] = particleswarm(@Obj_funMultiVar, narvs, x_lb, x_ub,options)
toc