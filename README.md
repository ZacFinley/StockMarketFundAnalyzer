To get the fund ticker symbols go to: https://www.marketwatch.com/tools/mutual-fund/list/A

CREATE DATABASE USA_Funds;

USE USA_Funds;

CREATE TABLE funds
(
ticker VARCHAR(5),
name TINYTEXT,
price DOUBLE(10,2),
expence_ratio_percent DOUBLE(5,2),
category TINYTEXT,
morning_star_rating SMALLINT,
net_assets TINYTEXT,
holdings_turnover_percent DOUBLE(5,2),
inception_date DATE,
fund_family TINYTEXT,
port_comp_cash_percent DOUBLE(5,2),
port_comp_stocks_percent DOUBLE(5,2),
port_comp_bonds_percent DOUBLE(5,2),
port_comp_others_percent DOUBLE(5,2),
port_comp_preferred_percent DOUBLE(5,2),
port_comp_convertable_percent DOUBLE(5,2),
sec_weight_basic_materials_percent DOUBLE(5,2),
sec_weight_consumer_cyclical_percent DOUBLE(5,2),
sec_weight_financial_services_percent DOUBLE(5,2),
sec_weight_realestate_percent DOUBLE(5,2),
sec_weight_consumer_defensive_percent DOUBLE(5,2),
sec_weight_healthcare_percent DOUBLE(5,2),
sec_weight_utilities_percent DOUBLE(5,2),
sec_weight_communication_services_percent DOUBLE(5,2),
sec_weight_energy_percent DOUBLE(5,2),
sec_weight_industrials_percent DOUBLE(5,2),
sec_weight_technology_percent DOUBLE(5,2),
perf_num_yrs_up SMALLINT(4),
perf_num_yrs_down  SMALLINT(4),
perf_ytd_percent DOUBLE(5,2),
perf_one_mon_percent DOUBLE(5,2),
perf_three_mon_percent DOUBLE(5,2),
perf_one_yr_percent DOUBLE(5,2),
perf_three_yr_percent DOUBLE(5,2),
perf_five_yr_percent DOUBLE(5,2),
perf_ten_yr_percent DOUBLE(5,2),
perf_life_percent DOUBLE(5,2),
min_init_inv INT,
min_subsequent_inv SMALLINT(4),
mutual_fund BOOLEAN,
etf BOOLEAN,
capture_date DATE
);
