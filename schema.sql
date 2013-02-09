drop table if exists menu;
create table menu (
  id integer primary key autoincrement,
  name string not null,
  date integer not null,
  meal string not null,
  servery_id int not null
);

drop table if exists serveries;
create table serveries (
  id integer primary key autoincrement,
  name string not null
);

insert into serveries(name) values ('north');
insert into serveries(name) values ('south');
insert into serveries(name) values ('east');
insert into serveries(name) values ('west');
insert into serveries(name) values ('sidrich');
insert into serveries(name) values ('baker');
