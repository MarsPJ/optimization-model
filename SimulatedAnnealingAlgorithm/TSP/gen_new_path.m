function path1 = gen_new_path(path0)
    % path0: ԭ����·��
    n = length(path0);
    % ���ѡ�����ֲ�����·���ķ���
    p1 = 0.33;  % ʹ�ý�����������·���ĸ���
    p2 = 0.33;  % ʹ����λ��������·���ĸ���
    r = rand(1); % �������һ��[0 1]����ȷֲ��������
    if  r< p1    % ʹ�ý�����������·�� 
        c1 = randi(n);   % ����1-n�е�һ���������
        c2 = randi(n);   % ����1-n�е�һ���������
        path1 = path0;  % ��path0��ֵ����path1
        path1(c1) = path0(c2);  %�ı�path1��c1��λ�õ�Ԫ��Ϊpath0��c2��λ�õ�Ԫ��
        path1(c2) = path0(c1);  %�ı�path1��c2��λ�õ�Ԫ��Ϊpath0��c1��λ�õ�Ԫ��
    elseif r < p1+p2 % ʹ����λ��������·��
        c1 = randi(n);   % ����1-n�е�һ���������
        c2 = randi(n);   % ����1-n�е�һ���������
        c3 = randi(n);   % ����1-n�е�һ���������
        sort_c = sort([c1 c2 c3]);  % ��c1 c2 c3��С��������
        c1 = sort_c(1);  c2 = sort_c(2);  c3 = sort_c(3);  % c1 < = c2 <=  c3
        tem1 = path0(1:c1-1);
        tem2 = path0(c1:c2);
        tem3 = path0(c2+1:c3);
        tem4 = path0(c3+1:end);
        path1 = [tem1 tem3 tem2 tem4];
    else  % ʹ�õ��÷�������·��
        c1 = randi(n);   % ����1-n�е�һ���������
        c2 = randi(n);   % ����1-n�е�һ���������
        if c1>c2  % ���c1��c2�󣬾ͽ���c1��c2��ֵ
            tem = c2;
            c2 = c1;
            c1 = tem;
        end
        tem1 = path0(1:c1-1);
        tem2 = path0(c1:c2);
        tem3 = path0(c2+1:end);
        path1 = [tem1 fliplr(tem2) tem3];   %��������ҶԳƷ�ת fliplr�����¶ԳƷ�ת flipud
    end
end