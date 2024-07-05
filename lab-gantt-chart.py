# Carney Lab Timeline (Gantt Chart)
# ported to Python and inspired by Prof. Janet E. Hill @HillLabSask
# original code in R - https://github.com/HillLabSask/HillLab_gantt_chart/

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams
from datetime import datetime, timedelta
from enum import Enum

LABTITLE = "Carney Lab"
LABSTARTDATE = datetime(2017, 12, 1)

class Role(Enum):
    PI = ("Principal Investigator", "#762a83")
    PhD_Student = ("Ph.D. Student", "#7fbf7b")
    PhD_Rotation_Student = ("PhD Rotation Student", "#17becf")
    Undergrad_Student = ("Undergraduate Student", "#de77ae")
    MS_Student = ("M.S. Student", "#d9f0d3")
    Postdoc = ("Postdoc", "#1b7837")
    Project_Scientist = ("Project Scientist", "#3377BB")
    Lab_Manager = ("Lab Manager/R&D Engineer", "#af8dc3")
    Technician = ("Technician/Research Assistant", "#e7d4e8")
    Visiting_Student = ("Visiting Student", "#ffcc99")

    def __init__(self, label, color):
        self.label = label
        self.color = color

def get_today_date_str(): # For "end" date of current lab members
    return datetime.today().strftime("%Y/%m/%d")

# Initialize and sort lab members
lab_members = [
    {"name": "Randy Carney", "periods": [
        {"start": "2018/07/01", "end": get_today_date_str(), "role": Role.PI}
    ]},
    {"name": "Hanna Koster", "periods": [
        {"start": "2018/09/24", "end": "2022/09/30", "role": Role.PhD_Student}
    ]},
    {"name": "Rachel Mizenko", "periods": [
        {"start": "2018/09/25", "end": "2019/01/04", "role": Role.PhD_Rotation_Student},
        {"start": "2019/03/15", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Victor Chiu", "periods": [
        {"start": "2018/10/25", "end": "2019/09/24", "role": Role.Undergrad_Student},
        {"start": "2019/09/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Nhi Trinh", "periods": [
        {"start": "2019/01/20", "end": "2020/04/30", "role": Role.Undergrad_Student},
    ]},
    {"name": "Hannah O'Toole", "periods": [
        {"start": "2019/01/20", "end": "2020/06/01", "role": Role.Undergrad_Student},
        {"start": "2020/09/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Marissa Taub", "periods": [
        {"start": "2019/03/25", "end": "2021/06/10", "role": Role.MS_Student}
    ]},
    {"name": "Dina Pham", "periods": [
        {"start": "2019/05/19", "end": "2020/12/15", "role": Role.Undergrad_Student}
    ]},
    {"name": "Alyssa Powell", "periods": [
        {"start": "2019/05/28", "end": "2021/02/03", "role": Role.Undergrad_Student}
    ]},
    {"name": "Henna Mohabbat", "periods": [
        {"start": "2019/06/12", "end": "2021/08/21", "role": Role.Undergrad_Student}
    ]},
    {"name": "Tatu Rojalin", "periods": [
        {"start": "2019/12/01", "end": "2021/12/31", "role": Role.Postdoc},
        {"start": "2022/01/01", "end": "2022/08/12", "role": Role.Project_Scientist}
    ]},
    {"name": "Lauren Gloekler", "periods": [
        {"start": "2019/11/19", "end": "2022/06/22", "role": Role.MS_Student}
    ]},
    {"name": "Terza Brostoff", "periods": [
        {"start": "2020/05/01", "end": "2023/04/30", "role": Role.Postdoc}
    ]},
    {"name": "Anna Kolesov", "periods": [
        {"start": "2021/09/19", "end": "2024/06/22", "role": Role.Undergrad_Student}
    ]},
    {"name": "Visha Arun", "periods": [
        {"start": "2021/09/13", "end": "2024/06/20", "role": Role.Undergrad_Student}
    ]},
    {"name": "Neona Lowe", "periods": [
        {"start": "2021/09/20", "end": "2021/10/22", "role": Role.PhD_Rotation_Student},
        {"start": "2022/03/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Bryan Nguyen", "periods": [
        {"start": "2021/10/25", "end": "2022/02/05", "role": Role.PhD_Rotation_Student},
        {"start": "2022/03/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Madison Feaver", "periods": [
        {"start": "2022/06/16", "end": "2023/09/20", "role": Role.Undergrad_Student}
    ]},
    {"name": "Batuhan Bozkurt", "periods": [
        {"start": "2023/01/02", "end": "2023/02/10", "role": Role.PhD_Rotation_Student},
        {"start": "2023/03/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Kuan-Wei Huang", "periods": [
        {"start": "2023/01/09", "end": "2023/02/10", "role": Role.PhD_Rotation_Student},
        {"start": "2023/03/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Samantha Ono", "periods": [
        {"start": "2023/01/10", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Bec Mayer", "periods": [
        {"start": "2022/11/29", "end": "2022/12/31", "role": Role.PhD_Rotation_Student},
        {"start": "2023/01/09", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Dustin Hadley", "periods": [
        {"start": "2023/03/31", "end": get_today_date_str(), "role": Role.Lab_Manager}
    ]},
    {"name": "Qing He", "periods": [
        {"start": "2023/04/01", "end": get_today_date_str(), "role": Role.Postdoc}
    ]},
    {"name": "Charuthi Arul", "periods": [
        {"start": "2023/05/06", "end": get_today_date_str(), "role": Role.Undergrad_Student}
    ]},
    {"name": "Anchaleena James", "periods": [
        {"start": "2023/07/17", "end": "2024/06/25", "role": Role.Undergrad_Student},
        {"start": "2024/06/26", "end": get_today_date_str(), "role": Role.Technician}
    ]},
    {"name": "Yifei Gu", "periods": [
        {"start": "2023/09/05", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Anastasia Trushchankova", "periods": [
        {"start": "2023/09/08", "end": get_today_date_str(), "role": Role.Undergrad_Student}
    ]},
    {"name": "David Meshkanian", "periods": [
        {"start": "2023/09/23", "end": get_today_date_str(), "role": Role.Undergrad_Student}
    ]},
    {"name": "Abigail Humphries", "periods": [
        {"start": "2023/09/25", "end": "2024/6/30", "role": Role.MS_Student},
        {"start": "2024/07/01", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Izabella Cristina Costa Ferreira", "periods": [
        {"start": "2023/11/01", "end": "2024/04/30", "role": Role.Visiting_Student}
    ]},
    {"name": "Elizabeth Hale", "periods": [
        {"start": "2024/01/08", "end": "2024/03/22", "role": Role.PhD_Rotation_Student},
        {"start": "2024/03/25", "end": get_today_date_str(), "role": Role.PhD_Student}
    ]},
    {"name": "Regina Rajbanshi", "periods": [
        {"start": "2024/01/15", "end": get_today_date_str(), "role": Role.Undergrad_Student}
    ]},
    {"name": "Nora Reed", "periods": [
        {"start": "2024/06/15", "end": get_today_date_str(), "role": Role.PhD_Rotation_Student}
    ]} 
]

rcParams['font.sans-serif'] = ['Helvetica'] # Set global font properties

def create_handles(roles):
    return [plt.Rectangle((0,0),1,1, color=role.color, label=role.label) for role in Role]

def parse_dates(lab_members):
    for member in lab_members:
        for period in member['periods']:
            period['start'] = datetime.strptime(period['start'], "%Y/%m/%d")
            period['end'] = datetime.strptime(period['end'], "%Y/%m/%d")
            
def plot_gantt_chart(lab_members):
    fig, ax = plt.subplots(figsize=(15, 7))
    handles = create_handles(Role)

    for i, member in enumerate(sorted(lab_members, key=lambda x: min(period['start'] for period in x['periods']), reverse=True)):
        name = member['name']
        periods = sorted(member['periods'], key=lambda x: x['start'])  # Sort periods by start date
        first_period = True  # Flag to only label the first period

        for period in periods:
            start_date = period['start']
            duration = (period['end'] - period['start']).days
            color = period['role'].color
            ax.barh(i, duration, left=start_date, color=color, edgecolor='black', linewidth=0.5, zorder=3)
            
            
            # Place text in front of the first bar only
            if first_period:
                padded_position = start_date - timedelta(days=5)  # Increase or decrease days for more or less padding
                ax.text(padded_position, i, name, va='center', ha='right', color='black', fontsize=10, family='sans-serif')
                first_period = False  # Update flag so only the first period for each person has a label
            
    ax.set_title(LABTITLE)
    ax.set_xlim(LABSTARTDATE, None)
    ax.set_yticks([])
    ax.set_yticklabels([])
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.grid(which='both', axis='x', linestyle=':', color='grey', alpha=0.5, zorder=0)
    ax.grid(which='both', axis='y', visible=False)
    ax.axvline(datetime.today(), color='black', linewidth=1, linestyle='--', label='Today')
    handles = [plt.Rectangle((0,0),1,1, color=role.color, label=role.label) for role in Role]
    plt.legend(handles=handles, title="Roles", loc='lower left', bbox_to_anchor=(0.05, 0.05), frameon=True)

    plt.tight_layout()
    plt.show()


parse_dates(lab_members)

plot_gantt_chart(lab_members)
