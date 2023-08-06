function y = Obj_funMultiVar(x)
    if check(x)
         disp("y");
%          f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
            y = 21.5+x(1)*sin(4*pi*x(1))+x(2)*sin(20*pi*x(2));
            y = -y;
%          y = x(1)^2+x(2)^2-x(1)*x(2)-10*x(1)-4*x(2)+60;
    else
        disp("n");
        y = 2000000;
    end
end