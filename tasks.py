from textwrap import dedent
from crewai import Task


class Tasks():

    def research_task(self, topic, agent):
        return Task(
            description=dedent(
                f"""
                Analyze the current industry trends, challenges, and opportunities relevant to the {topic}.

                Consider market reports, recent developments, and expert opinions to provide a comprehensive overview of the landscape related to {topic}.

                """),
            expected_output="A numbered list of 5 themes related to the topic.",
            agent=agent
        )

    def technical_writer_task(self, topic, agent):
        return Task(
            description=dedent(
                f"""
                Develop strategic talking points, questions, and discussion angles about {topic} using the research and industry analysis conducted.

                Write it in a way that is attention-grabbing and informative.

                """),
            expected_output='json format: {"research_summary": "less than 400 word summary of reearch"}',
            agent=agent
        )

    def gtm_task(self, topic, agent):
        return Task(
            description=dedent(
                f"""
                Develop a go-to-market strategy for a product or business related to {topic}.

                Identify the target audience that would most resonate with this plan. Try to group audiences with attributes that can be targeted on digital ad platforms.

                Identify the most effective channels to reach the target audience with this plan. Consider social media platforms, email newsletters, podcasts, and other digital channels. Make sure the list of channels is ranked in order of importance.

                Most importantly, this plan should include a detailed analysis of the target audience and the most effective channels to reach them.

                """),
            expected_output='json format: {"target_audience": "less than 200 word description of target audience", "channels": ["most important channel", "second most important channel", "third most important channel"]}',
            agent=agent
        )

    def social_media_writer_task(self, topic, agent):
        return Task(
            description=dedent(
                f"""
                Generate 5 hot takes related to {topic} that can be posted on Twitter. Hot takes are opinions that take a side on generally controversial topics. A good hot take is always backed by real data and facts. Never make up facts in a hot take.

                Below are some examples of well written hot takes:

                Topic: Cryptocurrency on Ethereum, Solana, and Bitcoin
                - Crypto won't win hearts and minds by debating semantics. We win by building apps that millions of people love.
                - Solana essentially becomes “the Eth of this cycle.” This isn't a flash in the pan, the outperformance will continue.
                - 60% of liquid stakers will opt into restaking (and eventually liquid restaking). This will be driven by reduced consensus and execution level rearwards, essentially pushing yield seekers out on the risk spectrum.
                - Ethereum's stake rate will go over 50% in 2024.
                - Ethereum pivots away from the “Ultrasound Money” meme and a new narrative will form.
                - Blast's lead will prompt other L2s and other similar looking protocols to offer native yield. Starting gun is fired when the chain goes live and TVL is way sticker than everyone thinks it will be.
                - Tribalism will get worse before it gets better. The industry will feel both bigger and more fractured than it does today.

                Topic: Boeing airlines
                - Boeing's quality control issues are a classic case of "too big to fail" syndrome. They've become so behemoth that they're too afraid to admit mistakes, leading to a culture of secrecy and cover-ups. Until they prioritize transparency, safety will always be at risk.
                - The real issue with Boeing's quality control isn't just the lack of oversight – it's the toxic work environment created by prioritizing profits over people. When employees are pushed to meet unrealistic deadlines, mistakes become inevitable. It's time for a culture shift that puts safety and accountability first.
                - Boeing's response to their quality control issues has been an exercise in damage control. They're more focused on saving face than actually fixing the problems. Until they take a real look at themselves and admit their shortcomings, the public will remain skeptical of their claims to have "learned from mistakes."
                - The FAA's oversight role is like being the kid who says "you can't catch me!" Boeing has consistently pushed the boundaries, exploiting loopholes and playing by their own rules. Until there are real consequences for non-compliance, quality control issues will persist.
                - In a world where tech giants like Tesla and SpaceX are revolutionizing industries with innovative designs and rigorous testing, why can't Boeing do the same? The answer lies in their outdated business model – they're more concerned with protecting their bottom line than investing in research and development. It's time for a reboot.

                """),
            expected_output='json format: {"hot_takes": ["hot_take1", "hot_take2", "hot_take3", "hot_take4", "hot_take5"]}',
            agent=agent
        )

    def summarize_task(self, agent):
        return Task(
            description=dedent(
                f"""
                Combine the outputs from the technical writer, social media writer, and gtm director.
                """),
            expected_output='json format: {"research_summary": "less than 400 word summary of reearch", "hot_takes": ["hot_take1", "hot_take2", "hot_take3", "hot_take4", "hot_take5"], "target_audience": "less than 400 word descriptino of target audience", "channels": ["most important channel", "second most important channel", "third most important channel"]}',
            agent=agent
        )
