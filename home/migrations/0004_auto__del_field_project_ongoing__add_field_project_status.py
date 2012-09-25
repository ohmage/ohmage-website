# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.ongoing'
        db.delete_column('home_project', 'ongoing')

        # Adding field 'Project.status'
        db.add_column('home_project', 'status',
                      self.gf('django.db.models.fields.CharField')(default='Current', max_length=60),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.ongoing'
        db.add_column('home_project', 'ongoing',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Project.status'
        db.delete_column('home_project', 'status')


    models = {
        'home.project': {
            'Meta': {'object_name': 'Project'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'collaborators': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '600'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Current'", 'max_length': '60'})
        }
    }

    complete_apps = ['home']