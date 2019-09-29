import matplotlib.pyplot as plt
import numpy as np


def acceleration(x, v, k=1, c=1):
    return -k * x - c * v


def euler_step(x_old, v_old, dt, k=1, c=1, alpha=1):
    a = acceleration(x_old, v_old, k=k, c=c)
    v_new = v_old + a * dt
    x_new = x_old + ((1 - alpha) * v_new + alpha * v_old) * dt
    return (x_new, v_new)


def euler(k=1, c=0, x0=0, v0=1, dt=1, t_max=10, t_0=0):
    x_old, v_old = x0, v0
    ts = []
    vs = []
    xs = []
    t = 0
    while t < t_max:
        x_new, v_new = euler_step(x_old, v_old, dt, k=k, c=c)
        xs.append(x_new)
        vs.append(v_new)
        ts.append(t)
        x_old = x_new
        v_old = v_new
        t += dt
    return (ts, xs, vs)


k = 10
c = 0.1
dt = .01
ts, xs, vs = euler(k=k, c=c, x0=1, v0=0, dt=dt, t_max=10, t_0=0)
fig, axes = plt.subplots(nrows=2, ncols=1)

# plot x
ax = axes[0]
ax.plot(ts, xs, label='x')
ax.set_xlabel("time")
ax.set_ylabel("position")
ax.legend()

# plot v
ax = axes[1]
ax.plot(ts, vs, label='x', color='orange')
ax.set_xlabel("time")
ax.set_ylabel("velocity")
ax.legend()
fig.tight_layout()

fig.savefig("euler-k-{:04.2f}-c-{:04.2f}-dt-{:04.2f}.png".format(k, c, dt))
