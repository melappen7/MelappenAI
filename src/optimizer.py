def optimize(cpu_usage, cost):
    # basic rule: reduce cost when usage is low
    decisions = []

    for u, c in zip(cpu_usage, cost):
        if u < 50:
            decisions.append("reduce_compute")
        else:
            decisions.append("keep_running")

    return decisions
