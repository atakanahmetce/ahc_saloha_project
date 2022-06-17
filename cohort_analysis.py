import datetime

def get_analysis(members, start_date, end_date):
    """
    Provide cohort result.
    """

    df = pd.DataFrame(members)
    cohort = pd.DataFrame()
    cohort["account"] = df[10]

    year_month_day = lambda x: datetime.datetime(x.year, x.month, x.day)

    # applying lambda function to data
    cohort["join_days"] = df[6].apply(year_month_day)

    today = datetime.date.today()
    delta = today - datetime.date(2022, 5, 1)
    total_day = delta.days + 1
    tomorrow = today + datetime.timedelta(days=1)

    exit_days = []
    for exit_day in df[7]:
        if str(exit_day) != "NaT":
            exit_days.append(exit_day.strftime("%Y-%m-%d"))
        else:
            exit_days.append(tomorrow.strftime("%Y-%m-%d"))
    cohort["exit_days"] = exit_days

    # clean before may of 1.
    cohort.drop(
        cohort[cohort["join_days"] < pd.Timestamp(datetime.date(2022, 5, 1))].index,
        inplace=True,
    )


    cohort.sort_values(by="join_days")
    cohort = cohort.groupby("join_days")

    incoming_users = []

    header = [i for i in range(total_day)]
    chart_data = pd.DataFrame(columns=["users"] + header)
    chart_data_percentege = pd.DataFrame(columns=["users"] + header)


    for i in cohort:

        incoming_users.append(len(i[1]))

        tmp_retention = []
        tmp_retention.append(len(i[1]))

        group_size = len(i[1])
        tmp_retention_percent = []
        tmp_retention_percent.append(len(i[1]))

        tmp_number_of_members = len(i[1])

        i[1].sort_values(by="exit_days")
        tmp = i[1].groupby("exit_days")

        number_of_losts = {}
        for j in tmp:
            if j[0] == tomorrow.strftime("%Y-%m-%d"):
                # user still active
                continue

            number_of_losts[j[0]] = len(j[1])

        ranges = total_day + 1
        for x in range(ranges):
            calculating_date = i[0] + datetime.timedelta(days=x)
            if calculating_date > today:
                break
            calculating_date = calculating_date.strftime("%Y-%m-%d")

            if calculating_date in number_of_losts:
                tmp_number_of_members -= number_of_losts[calculating_date]
            tmp_retention.append(tmp_number_of_members)
            percent = (tmp_number_of_members * 100) / group_size
            percent = round(percent, 2)
            tmp_retention_percent.append(percent)

        while x < total_day:
            tmp_retention.append(np.NAN)
            tmp_retention_percent.append(np.NAN)
            x += 1

        chart_data.loc[i[0].strftime("%m-%d")] = tmp_retention
        chart_data_percentege.loc[i[0].strftime("%m-%d")] = tmp_retention_percent

    plt.figure(figsize=(20, 20))
    plt.title("Retention Analysis")
    sns.heatmap(chart_data, annot=True, vmin=0.0, vmax=100, cmap="YlGnBu", fmt="g")
    plt.yticks(rotation="360")
    # plt.show()
    plt.savefig(str(today) + ".png")

    # chart_data.to_csv("deneme.csv", sep=",")

    plt.figure(figsize=(20, 20))
    plt.title("Retention Analysis")
    sns.heatmap(
        chart_data_percentege, annot=True, vmin=0.0, vmax=100, cmap="YlGnBu", fmt="g"
    )
    plt.yticks(rotation="360")
    plt.savefig(str(today) + "_percent.png")

    chart_data.to_excel(str(today) + ".xlsx")
    chart_data_percentege.to_excel(str(today) + "_percent.xlsx")
