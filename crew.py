from crewai import Crew
from agents import Agents
from tasks import Tasks


class TheCrew:

    def start_crew(self, topic):
        agents = Agents()
        tasks = Tasks()

        # Agents
        research_agent = agents.researcher()
        social_media_writer = agents.social_media_writer()
        technical_writer = agents.technical_writer()
        summarizer_agent = agents.summarizer_agent()
        gtm_director = agents.gtm_director()

        # Tasks
        research_task = tasks.research_task(topic, research_agent)
        social_media_writer_task = tasks.social_media_writer_task(
            topic, social_media_writer)
        technical_writer_task = tasks.technical_writer_task(
            topic, technical_writer)
        gtm_task = tasks.gtm_task(topic, gtm_director)
        summarize_task = tasks.summarize_task(
            summarizer_agent
        )

        # Instantiate your crew
        crew = Crew(
            agents=[research_agent, social_media_writer,
                    technical_writer, gtm_director, summarizer_agent],
            tasks=[research_task, social_media_writer_task,
                   technical_writer_task, gtm_task, summarize_task],
        )

        # Start the crew's work
        result = crew.kickoff()
        return result
