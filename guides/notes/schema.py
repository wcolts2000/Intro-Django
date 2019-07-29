from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note, PersonalNote

from graphene_django.filter import DjangoFilterConnectionField


class PersonalNoteType(DjangoObjectType):

    class Meta:
        model = PersonalNote
        interfaces = (graphene.relay.Node,)
        # filter_fields = ['title', 'content']
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'content': ['exact', 'icontains'],
        }


class NoteType(DjangoObjectType):

    class Meta:
        model = Note
        interfaces = (graphene.relay.Node,)
        # filter_fields = ['title', 'content']
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'content': ['exact', 'icontains'],
        }


class Query(graphene.ObjectType):
    notes = DjangoFilterConnectionField(NoteType)
    # notes = graphene.List(NoteType)

    # # Note the resolve liine here must match teh name of the List (line 17)
    # def resolve_notes(self, info):
    #     return Note.objects.all()


class CreateNote(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    note = graphene.Field(NoteType)
    ok = graphene.Boolean()

    def mutate(self, info, title, content):
        new_note = Note(title=title, content=content)
        new_note.save()

        return CreateNote(note=new_note, ok=True)


class CreatePersonalNote(graphene.Mutation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    personalnote = graphene.Field(PersonalNoteType)
    ok = graphene.Boolean()

    def mutate(self, info, title, content):
        logged_in_user = info.context.user
        new_note = PersonalNote(
            title=title, content=content, user=logged_in_user)
        new_note.save()

        return CreatePersonalNote(personalnote=new_note, ok=True)


class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()
    create_personal_note = CreatePersonalNote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
