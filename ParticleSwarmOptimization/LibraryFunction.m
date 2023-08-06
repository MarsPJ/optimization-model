%% Matlab�Դ�������Ⱥ���� particleswarm
% particleswarm����������Сֵ��
% ���Ŀ�꺯���������ֵ����Ҫ��Ӹ��ŴӶ�ת��Ϊ����Сֵ��
clear;clc
%% ��⺯��y = x1^2+x2^2-x1*x2-10*x1-4*x2+60��[-15,15]�ڵ���Сֵ����СֵΪ8��
narvs = 2; % ��������
% x_lb = [-15 -15]; % x���½�(���ȵ��ڱ����ĸ�����ÿ��������Ӧһ���½�Լ��)
% x_ub = [15 15]; % x���Ͻ�
x_lb = [-3 4.1]; % x���½�(���ȵ��ڱ����ĸ�����ÿ��������Ӧһ���½�Լ��)
x_ub = [12.1 5.8]; % x���Ͻ�
options = optimoptions('particleswarm',...
'PlotFcn','pswplotbestf',...% ������ѵĺ���ֵ����������ı仯ͼ
'SwarmSize',50,...% �޸�����������Ĭ�ϵ��ǣ�min(100,10*nvars)
'HybridFcn',@fmincon,... % ������Ⱥ�㷨������������������������л�����
'InertiaRange',[0.2 1.2],... % ����Ȩ�صı仯��Χ��Ĭ�ϵ���0.1-1.1
'SelfAdjustmentWeight',2,...% ����ѧϰ���ӣ�Ĭ�ϵ���1.49��ѹ�����ӣ�
'SocialAdjustmentWeight',2,...% ���ѧϰ���ӣ�Ĭ�ϵ���1.49��ѹ�����ӣ�
'MaxIterations',1000,...% ���ĵ���������Ĭ�ϵ���200*nvars
'MinNeighborsFraction',0.2,...% ���������ӵı��� MinNeighborsFraction��Ĭ����0.25 
'FunctionTolerance',1e-8,...% �������̶�FunctionTolerance, Ĭ��1e-6, ���ڿ����Զ��˳������Ĳ���
'MaxStallIterations',50);% ���ͣ�͵�����MaxStallIterations, Ĭ��20, ���ڿ����Զ��˳������Ĳ���

% 'Display','iter'% չʾ�����ĵ�������

tic
[x,fval,exitflag,output] = particleswarm(@Obj_funMultiVar, narvs, x_lb, x_ub,options)
toc