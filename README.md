# Euler Method 

In mechanics, we often use Euler’s method to determine the motion of an object given how the acceleration depends on the velocity and position of an object. For example, we may know that the acceleration $a(x, v)$ is given as:

$$a(x, v) = −kx − cv$$

If we know the position $x$ and the velocity $v$ at a time $t = 0$, $x(0) = x_0 = 0$ and $v(0) = v_0 = 1$ 

we can use Euler’s method to find the position and velocity after a small timestep ∆t:
$$
v_n = v(t_{n-1} + ∆t) = v(t_{n-1}) + a(v(t_{n-1}), x(t_{n-1}))∆t\\
x_n = x(t_{n-1} + ∆t) = x(t_{n-1}) + v(t_{n-1})∆t
$$
We can therefore use this scheme to find the position $x(t)$ and the velocity $v(t)$ as a function of time at the discrete values $t_i = i∆t$ in time.

(a) Write a function `acceleration(v,x,k,C)` which returns the value of $a(x, v)$

(b) Write a function `euler_step(x_old,v_old,dt,k=1,c=.01)` returning `x_new,v_new`, the values of the position and velocity at the next time step, given the position and velocity at the previous step, and the equation parameters.

(b) Write a function `euler(k=1,c=0,x0=0,v0=1,dt=.01,t_0=0,t_max=10)` returning three arrays `(ts,xs,ys)` with the values of the time, position, and velocity, given the initial condition and the system parameters (`dt` is the time step, `t_max`the maximum integration time and `t_0` the initial time). 

(c) For `k=10`, `c=0.10`, `t_max=10` save to a file a plot including two subplots with the plot of the position and velocity. Add suitable axes name, legend, and title. 
Try to generate file names for the figure of the type `euler-k-0.10-c-0.10-dt-0.01.png` 
where the numbers are the values of the parameters (see https://pyformat.info). 
Make the position plot blue and the velocity plot orange.

(d) Is the choice of the time step `dt` important? Try to review your undergraduate class on this topic and porpduce a figure that illustrate the influence of `dt`. Include a caption for the figure explaining the finding.

We ask to submit

1 - The figure of part (c)

2 - The figure of part (d), with the caption. 

3 - A script `euler.py`, which should produce the two figures when executed. 

We will evaluate the following points:

* Does the code run wihtout error?

* Does the code  produce the correct results?

* Are the figures clear and respect the requirements?

* Is the PEP8 codying style respected? (see http://sametmax.com/le-pep8-en-resume/)

Note: You can check automatically the codying style in several way. For example online: http://pep8online.com. There are also several tools for automatic formatting, e.g. https://pypi.org/project/autopep8/.
