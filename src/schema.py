#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import graphene
import json

class plotInputType(graphene.InputObjectType):
  kind = graphene.List(graphene.String,default_value=None)
  category = graphene.List(graphene.String,default_value=None)

class PlotType(graphene.ObjectType):
  object_id = graphene.ID()
  kind = graphene.String()
  category = graphene.String()

class ScatterPlotAccountType(PlotType):
  id = graphene.Int()
  name = graphene.String()
  x = graphene.Int()
  y = graphene.Int()

  @property
  def coordinate(self):
    return {"x":self.x,"y":self.y}

class Query(graphene.ObjectType):
    account_plots = graphene.List(ScatterPlotAccountType, p_filter=plotInputType())
    @staticmethod
    def resolve_account_plots(root, info, p_filter):
      p_fltr = dict(filter(lambda x: x[1] != None ,p_filter.items()))
      #   #TODO p_fltr.keys()で動的に判定する
      #   if row["category"] in list(p_fltr["category"]) and row["kind"] in list(p_fltr["kind"]):
      #     print(row)
      return [ScatterPlotAccountType(id=0,
        name = row["name"],
        category = row["category"],
        kind=row["kind"],
        x=row["x"],
        y=row["y"]
        ) for row in json.load(open("statics/sample_data_account.json","r")) if row["category"] in list(p_fltr.get("category",["food","beauty_and_cosmetics"])) and row["kind"] in list(p_fltr.get("kind",["user","follower"]))]

schema = graphene.Schema(query=Query)
